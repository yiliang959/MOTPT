# MOTPT — Agent Operating Rules (bootstrap v1)

## 1. Mandatory read order

1. `governance.json`
2. `AGENTS.md`
3. `docs/RESEARCH.md`
4. `docs/EVIDENCE.md`
5. `docs/CURRENT.md`
6. The single active research Issue / Draft PR, when one exists.

Authority priority: explicit Project Owner decision > tracked governance > scientific contract > accepted evidence > current control plane > active Issue/PR. Chat memory and a repository name are not scientific authority. Update canonical files **in place**, not in dated handoffs or parallel "latest" files.

## 2. Independent scientific scope

MOTPT is independent of TCR-MOT. Native MOTIP may be a common baseline. Matching source/dataset/failure cases does not imply matching research hypotheses, designs, scientific verdicts, or execution permission. Do not reverse-engineer a MOTPT scientific objective from TCR documents. **The Owner's preliminary trajectory-related intuition is discussion only; do not write or implement it before an explicit research freeze.** The current contract is UNDEFINED.

## 3. Current execution authority: HOLD

During bootstrap you may modify infrastructure/docs, run pure CPU static checks and synthetic unit tests, and review provenance without consuming benchmark data. No experimental Native/GPU forward, optimizer, training, dataset/VAL/TEST analysis or TrackEval, creation of a model architecture, or publishing scientific evidence/claims. A generic chat approval, borrowed TCR control-plane key, or completed CI is not execution authority.

Later releases require exact workstream, operation, dataset/split/population, checkpoint/config, allowed outputs, and stop conditions in tracked `governance.json` + `docs/CURRENT.md`, plus explicit Project Owner authorization. Official TEST is independently approved, never an implied consequence of having TEST files.

## 4. Information and evidence boundary

Separate `MODEL_VISIBLE`, `SUPERVISION_ONLY`, `ANALYSIS_ONLY`, and `EVALUATOR_ONLY`. Runtime uses current-frame information and strictly causal state only by default; GT, future information, oracle mappings, TrackEval states and private cross-repo evidence must not enter runtime inputs. Any departure needs a distinct scientific contract and Owner review.

Keep persistent output tracker IDs separate from recyclable MOTIP `id_label` slots. A detector-vs-GT overlap diagnostic is not automatically an IDSW, and GT annotations are not a complete continuous physical trajectory. Label findings `FACT`, `SUPPORTED_INFERENCE`, or `OPEN_HYPOTHESIS`, with exact source and population. Do not treat reuse of the same VAL failures across projects as independent corroboration.

## 5. Tier division

- **Owner:** final scientific authority, research freeze, scope/TEST/execution release, final merge/promotion.
- **Tier-1 (optional):** independent research escalation when called by Owner.
- **Tier-2:** designs and freezes the scientific contract, interpretation and final evidence; decides when a semantic change is needed.
- **Tier-3:** implements a frozen contract autonomously; owns debugging, tests, telemetry, organization, batching and non-semantic optimizations. Return to Tier-2 for changes to objective, model/dataflow, supervision, loss, data/evaluation population, causal boundary, result provenance, or a falsified scientific assumption.

## 6. Workflow and gates

Ordinarily one active research Issue + branch + Draft PR per research/model generation; no per-subtask PR proliferation. Governance maintenance may use a separate workstream. G0 scientific freeze → G1 CPU implementation self-audit → G2 separately authorized parity canary → G3 separately authorized TRAIN/VAL → G4 scientific adjudication → G5 Owner-reviewed closeout/merge/branch cleanup. New model versions require a material scientific change and explicit freeze. Diagnostic scripts do **not** automatically constitute a model generation.

Merged branch deletion and no force-push on shared/protected branches are default. No simultaneous research PRs without Owner exception.

## 7. Cross-repository reuse / public hygiene

See `docs/CROSS_REPO_REUSE.md`. Never directly import TCR modules at MOTPT runtime, mirror an entire TCR tree, or treat historical TCR results as MOTPT-accepted evidence. Port only minimal general utilities after reviewing exact source SHA, behavior/parity tests, license, dependencies, and public-release risk. MOTPT is PUBLIC: exclude private annotations, personal/server paths, tokens, raw datasets, private evidence, checkpoints, and large artifacts. Keep source provenance in the porting PR.

## 8. Working-tree discipline

Use `motpt/` for reusable Python, `scripts/` for thin entrypoints, `tests/` for regressions, `docs/` for canonical knowledge, optional `external/` only for actually needed pinned third-party code. Use small reviewed audit summaries in `docs/results/<workstream>/`, not raw output dumps. Do not create a `models/` or `training/` implementation before the Owner approves the scientific design.

## 9. Stop conditions

STOP and return to Owner/Tier-2 on missing experimental permission, provenance mismatch, unauthorized private-to-public copy, non-reproducible baseline, future/GT leakage, conflicting contract, unexpected TEST access, or a requested scientific assumption not yet defined. Ordinary engineering failures belong to Tier-3 unless they force a semantic change.
