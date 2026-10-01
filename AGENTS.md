# MOTPT — Agent Operating Rules

## 1. Mandatory read order

1. `governance.json`
2. `AGENTS.md`
3. `docs/RESEARCH.md`
4. `docs/EVIDENCE.md`
5. `docs/CURRENT.md`
6. The single active research Issue / Draft PR.

Authority priority: explicit Project Owner decision > tracked governance > scientific contract > accepted evidence > current control plane > active Issue/PR. Chat memory and a repository name are not scientific authority. Update canonical files **in place**, not in dated handoffs or parallel "latest" files.

## 2. Independent scientific scope

MOTPT is independent of TCR-MOT. Native MOTIP may be a common baseline. Matching source/dataset/failure cases does not imply matching research hypotheses, designs, scientific verdicts, or execution permission.

The Owner has approved the **v0 latent-flow-belief formulation for repository discussion and iterative refinement**. It is canonical working research context in `docs/RESEARCH.md`, but is **not** a final G0 method freeze. Do not invent representation, modules, losses, datasets or claims beyond the recorded working formulation.

## 3. Current execution authority: HOLD

During the G0 discussion phase you may modify research/governance docs, perform literature review, run pure CPU static checks and synthetic unit tests, and review provenance without consuming benchmark data.

No experimental Native/GPU forward, optimizer, training, dataset/VAL/TEST analysis or TrackEval, model implementation, or publication claim is authorized. A generic chat approval, borrowed TCR control-plane key, completed CI, or acceptance of the v0 concept is not execution authority.

Later releases require exact workstream, operation, dataset/split/population, checkpoint/config, allowed outputs and stop conditions in tracked `governance.json` + `docs/CURRENT.md`, plus explicit Project Owner authorization. Official TEST is independently approved.

## 4. Information and evidence boundary

Separate `MODEL_VISIBLE`, `SUPERVISION_ONLY`, `ANALYSIS_ONLY`, and `EVALUATOR_ONLY`. Runtime uses current-frame information and strictly causal state only by default; GT, future information, oracle mappings, TrackEval states and private cross-repo evidence must not enter runtime inputs.

Keep persistent output tracker IDs separate from recyclable MOTIP `id_label` slots. A detector-vs-GT overlap diagnostic is not automatically an IDSW, and GT annotations are not a complete continuous physical trajectory.

Label findings `FACT`, `SUPPORTED_INFERENCE`, `OPEN_HYPOTHESIS`, or `WORKING_FORMULATION`. A working formulation is an Owner-approved research direction, not empirical evidence.

## 5. Tier division

- **Owner:** final scientific authority, final G0 freeze, scope/TEST/execution release, final merge/promotion.
- **Tier-1 (optional):** independent research escalation when called by Owner.
- **Tier-2:** refines and freezes scientific contracts, interpretation and final evidence; decides when a semantic change is needed.
- **Tier-3:** implements a frozen contract autonomously; owns debugging, tests, telemetry, organization, batching and non-semantic optimizations. Return to Tier-2 for changes to objective, model/dataflow, supervision, loss, data/evaluation population, causal boundary, result provenance, or a falsified scientific assumption.

## 6. Workflow and gates

Ordinarily one active research Issue + branch + Draft PR per research/model generation; no per-subtask PR proliferation. Governance maintenance may use a separate workstream.

Current Issue #1 is a pre-freeze G0 discussion workstream.

Final G0 scientific freeze → G1 CPU implementation self-audit → G2 separately authorized parity canary → G3 separately authorized TRAIN/VAL → G4 scientific adjudication → G5 Owner-reviewed closeout/merge/branch cleanup.

New model versions require a material scientific change and explicit freeze. Diagnostic scripts do **not** automatically constitute a model generation.

## 7. Cross-repository reuse / public hygiene

See `docs/CROSS_REPO_REUSE.md`. Never directly import TCR modules at MOTPT runtime, mirror an entire TCR tree, or treat historical TCR results as MOTPT-accepted evidence.

Port only minimal general utilities after reviewing exact source SHA, behavior/parity tests, license, dependencies and public-release risk. MOTPT is PUBLIC: exclude private annotations, personal/server paths, tokens, raw datasets, private evidence, checkpoints and large artifacts.

## 8. Repository structure and knowledge discipline

`docs/STRUCTURE.md` is the canonical repository-shape contract.

Use the fixed top-level structure and update canonical Markdown **in place**. Git already preserves previous versions, so never create versioned/datetime/“latest” copies of `RESEARCH.md`, `CURRENT.md`, `EVIDENCE.md`, or other canonical docs.

Scientific evidence has exactly one ledger: `docs/EVIDENCE.md`. A new run, gate, negative result, dataset comparison or adjudication updates an existing/new entry in that file. Do not create per-run/per-issue/per-epoch evidence Markdown or `docs/results/<run>/` trees. Raw artifacts stay outside Git and are referenced by immutable hash/manifest/path.

The controlled exception is `docs/literature/papers/`: one note per distinct paper may be added, while the index and novelty matrix are still updated in place.

Use `motpt/` for reusable Python, `scripts/` for thin entrypoints and `tests/` for regressions. Prefer adding files to existing approved namespaces rather than creating directories. New top-level paths or new canonical files under `docs/` require explicit Owner approval.

Do not create model/training implementation before the final G0 contract and explicit implementation release. Research diagrams/pseudocode in `docs/RESEARCH.md` do not grant implementation permission.

Issues/PRs coordinate work; they are not the current knowledge base. Any decision that survives review must be written back to the owning canonical Markdown file before closeout.

## 9. Stop conditions

STOP and return to Owner/Tier-2 on missing experimental permission, provenance mismatch, unauthorized private-to-public copy, non-reproducible baseline, future/GT leakage, conflicting contract, unexpected TEST access, or a requested scientific assumption not yet defined.

Ordinary literature/doc refinement is allowed within the current workstream. Ordinary engineering failures belong to Tier-3 only after implementation authority exists.
