# MOTPT — Repository Structure Contract

```text
STATUS = FROZEN_V1
EXPANSION_POLICY = EXPLICIT_OWNER_DECISION_REQUIRED
KNOWLEDGE_MODEL = CANONICAL_MD_UPDATED_IN_PLACE
GIT_ROLE = HISTORY / DIFF / PROVENANCE / ERROR_RECOVERY
```

## 1. Purpose

MOTPT intentionally keeps a **small, stable repository shape**. The repository must not grow by creating a new directory, status document, evidence document, handoff file, or versioned copy every time the research changes.

The rule is:

> **Change the content of the canonical file; do not create another canonical-looking file. Git already preserves the old version.**

Git history exists to answer “what changed / when / why / how do we recover a mistake?”. It is **not** the project's current memory. The current research state must be readable from the canonical Markdown files without reconstructing commit history.

## 2. Frozen top-level structure

```text
MOTPT/
├── governance.json
├── AGENTS.md
├── CLAUDE.md
├── README.md
├── .gitignore
├── .github/
│   └── workflows/
├── docs/
│   ├── RESEARCH.md
│   ├── CURRENT.md
│   ├── EVIDENCE.md
│   ├── STRUCTURE.md
│   ├── BASELINE.md
│   ├── DATASETS.md
│   ├── DIAGNOSTICS.md
│   ├── CROSS_REPO_REUSE.md
│   └── literature/
│       ├── README.md
│       ├── NOVELTY_MATRIX.md
│       ├── PAPER_TEMPLATE.md
│       └── papers/
├── motpt/
│   ├── config/
│   ├── data/
│   ├── diagnostics/
│   ├── evaluation/
│   ├── model/       # reserved; create only after implementation release
│   └── runtime/     # reserved; create only after implementation release
├── scripts/
└── tests/
```

Empty reserved directories do not need to exist in Git. Their names are reserved so later implementation does not create arbitrary sibling namespaces.

No new top-level directory and no new canonical file directly under `docs/` may be created without an explicit Project Owner decision.

## 3. Canonical documents

| File | Single responsibility |
|---|---|
| `README.md` | entrypoint, short project identity, stable structure |
| `docs/RESEARCH.md` | one living scientific formulation / contract |
| `docs/CURRENT.md` | one current control plane: active issue/PR/task/permissions |
| `docs/EVIDENCE.md` | **one scientific evidence ledger** |
| `docs/BASELINE.md` | baseline identity / pins / parity state |
| `docs/DATASETS.md` | single dataset selection, role and verification checklist |
| `docs/DIAGNOSTICS.md` | diagnostic semantics and schemas |
| `docs/CROSS_REPO_REUSE.md` | cross-repository transfer policy |
| `docs/STRUCTURE.md` | this fixed structure / knowledge-management contract |
| `docs/literature/README.md` | literature taxonomy/index |
| `docs/literature/NOVELTY_MATRIX.md` | cross-paper novelty/collision comparison |

When one of these topics changes, **edit the file in place**.

## 4. Evidence rule — one ledger, not one file per experiment

`docs/EVIDENCE.md` is the only canonical scientific evidence document.

When a run, diagnostic, negative result, parity check or adjudication changes what is scientifically known:

1. update the appropriate section/entry in `docs/EVIDENCE.md`;
2. record immutable provenance there: source SHA, config/checkpoint/input hashes, dataset/split/population, evaluator, result/artifact hash or external artifact reference;
3. replace or mark the old interpretation as superseded **inside the same ledger**;
4. let Git history retain the previous wording.

Do **not** create:

```text
EVIDENCE_v2.md
EVIDENCE_final.md
EVIDENCE_issue12.md
evidence_run_001.md
evidence_epoch10.md
docs/results/<run>/README.md
handoff_evidence.md
latest_evidence.md
```

Raw logs, videos, checkpoints, large JSON/CSV dumps and run directories do not belong in Git. The ledger points to immutable artifacts by hash/manifest/path when needed.

A new standalone evidence document is permitted only if the Project Owner explicitly changes this structure contract.

## 5. Literature is the controlled exception

Literature naturally grows paper-by-paper. Therefore `docs/literature/papers/` may add **one note per distinct paper** using the existing template.

This exception does not allow:

- multiple versions of the same paper note;
- dated survey snapshots;
- separate “latest survey” files;
- evidence/results files under `docs/literature/`.

Update an existing paper note or the single novelty matrix in place.

## 6. Code structure rule

Prefer adding a file to an existing namespace over creating a new directory.

Allowed `motpt/` namespaces are limited to:

- `config/`
- `data/`
- `diagnostics/`
- `evaluation/`
- `model/` (reserved)
- `runtime/` (reserved)

Do not create generic dumping grounds such as `utils2/`, `misc/`, `common_new/`, `analysis_v2/`, `modules/`, or one directory per experiment.

A scientific experiment should normally change configuration/code and update `docs/EVIDENCE.md`; it should **not** create a new permanent package subtree.

## 7. Issue / PR / Git role

Issue and Draft PR are for coordination, review, discussion and gating. Before a decision is considered canonical, write it back to the appropriate canonical Markdown file.

Commits are for:

- history;
- diffs;
- provenance;
- reverting mistakes;
- tracing when a rule/result changed.

Do not require future agents to mine Git history, old PR comments or closed Issues to know the current state.

## 8. Naming and anti-proliferation rules

Forbidden by default:

- version suffixes for canonical documents: `_v2`, `_v3`, `_final`, `_latest`, `_new`;
- dated copies of canonical state;
- handoff/status snapshot stacks;
- one evidence Markdown per run/epoch/dataset;
- duplicate “current” files;
- archive folders whose only purpose is to keep previous Markdown versions.

If history is needed, use Git.

## 9. Change test

Before creating a new file/directory, ask:

1. Does an existing canonical file own this information?
2. Can this be a new section/entry instead of a new file?
3. Is the content a raw artifact that should stay outside Git?
4. Is the new path part of the frozen allowlist?
5. If not, has the Owner explicitly approved structure expansion?

If 1 or 2 is yes, **update in place**. If 3 is yes, store only its provenance/reference. If 4 is no and 5 is no, do not create it.
