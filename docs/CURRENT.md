# MOTPT — Canonical Current State

```text
STATE_ID = MOTPT-G1-20261001-V0-FORMULATION-DISCUSSION
REPOSITORY = yiliang959/MOTPT
ACTIVE_BRANCH = research/1-motpt-v0-formulation
ACTIVE_RESEARCH_ISSUE = #1
ACTIVE_RESEARCH_PR = #2
CURRENT_RESEARCH_CONTRACT = V0_CONCEPT_OWNER_ACCEPTED__NOT_G0_FROZEN
CURRENT_RESEARCH_HYPOTHESIS = PERSISTENT_OBJECT_SPECIFIC_LATENT_FLOW_BELIEF__WORKING_V0
CURRENT_ACCEPTED_MODEL = NONE
BASELINE = MOTIP_PLANNED__NOT_MOTPT_VALIDATED
DATASET_SELECTION = WORKING__SportsMOT_PRIMARY__DanceTrack_SECONDARY__BFT_STRESS_TEST
DATASET_CONTRACT = docs/DATASETS.md__NOT_G0_FROZEN
CURRENT_TASK = REFINE_PROBLEM_NOVELTY_MODULES_AND_G0_REQUIREMENTS
LITERATURE_LAYER = docs/literature/README.md__22_CORE_PAPERS
STRUCTURE_POLICY = FROZEN_V1__CANONICAL_MD_UPDATE_IN_PLACE
EVIDENCE_POLICY = SINGLE_LEDGER__docs/EVIDENCE.md
PRE_G0_REVIEW = PASS_WITH_FORMULATION_TIGHTENING__NO_EXECUTION_RELEASE
OWNER_DIRECTION_20261001 = MOT_PRIMARY__MTP_FEEDBACK__2D_PROJECTED__FUTURE_BELIEF_REFINEMENT
RETENTION_POLICY = OPEN__DATASET_DISTRIBUTION_STUDY_REQUIRED
PRE_EXPERIMENT_NOVELTY_RISK = DIFFUTRACK_DIRECT_COLLISION__PERSISTENT_REFINEMENT_REQUIRED
PRE_EXPERIMENT_REVIEW = CONDITIONAL_GO__PARITY_AND_DIAGNOSTICS_FIRST
EXECUTION_STATE = HOLD__G0_DISCUSSION_ONLY__NO_SCIENTIFIC_EXECUTION
SCIENTIFIC_EXECUTION = PROHIBITED
DATASET_CONSUMING_ANALYSIS = PROHIBITED
NATIVE_MODEL_FORWARD = PROHIBITED
GPU_MODEL_FORWARD = PROHIBITED
OPTIMIZER_STEP = PROHIBITED
TRAINING = PROHIBITED
ONLINE_VAL_INFERENCE = PROHIBITED
OFFICIAL_VAL_TRACKEVAL = PROHIBITED
OFFICIAL_TEST = PROHIBITED_UNTIL_SEPARATELY_AUTHORIZED
```

## Active workstream

Issue #1 tracks the living v0 formulation. The Owner approved writing the current concept into the repository and expects details to evolve with literature review and research.

Current core:

```text
current MOT belief/state
    -> multimodal MTP future prediction
    -> predictive signal returned to MOT
    -> next observation / association
    -> MOT belief update
    -> repeat
```

**MOT is the primary task.** MTP is an auxiliary predictive mechanism built from the current MOT state and fed back to improve MOT. The formal term is **Future Belief Refinement**. Stage 1 is **2D projected/image-space MOT**.

MOTPT does not impose a fixed observation window, but computational retention/termination is not assumed infinite. The retention policy remains open until track-lifetime, missing-gap and reappearance-gap distributions are measured under an authorized dataset diagnostic.

## Current scientific status

The formulation in `docs/RESEARCH.md` is accepted as the canonical **working concept**, not a final method or validated claim.

No dataset, model implementation, training objective, evaluation population or acceptance threshold is yet frozen. `docs/EVIDENCE.md` remains empty of accepted MOTPT scientific results.

## Next decisions before G0 freeze

1. tighten the mathematical representation of predictive belief and its uncertainty/multimodality semantics;
2. define minimal falsification tests and capacity-matched baselines;
3. select datasets/splits and specify the first authorized **track-lifetime / missing-gap / reappearance-gap distribution study**;
4. choose the MTP representation family and exact MOTIP integration/feedback point;
5. decide whether stage-1 image-space modeling needs explicit camera-motion compensation;
6. define losses, MOT-primary acceptance criteria and secondary MTP/refinement metrics;
7. freeze one minimal implementable contract before model execution.

Until then, literature review, docs/governance edits and synthetic/static tests are allowed; benchmark-consuming research execution is not.

## Literature layer

The active branch now contains a structured survey at `docs/literature/`: an index/taxonomy, a novelty collision matrix, a reusable paper-note template, and 22 per-paper extraction notes. These notes support Issue #1 and remain revisable as deeper reading changes the comparison.


## Repository structure policy

Repository shape is frozen by `docs/STRUCTURE.md`.

Current rule:
- canonical research/state/evidence documents are updated in place;
- Git preserves old versions and is not a second project-memory system;
- `docs/EVIDENCE.md` is the only scientific evidence ledger;
- do not create evidence/status/handoff/version stacks;
- raw experiment artifacts remain outside Git and are referenced by provenance;
- new top-level or canonical `docs/` paths require explicit Owner approval;
- literature paper notes are the controlled growth exception.


## Pre-experiment gate

Scientific review status: **CONDITIONAL GO**.

Before model training, the first released work should establish:

1. Native MOTIP parity on the exact pinned checkpoint/config/evaluator;
2. dataset distributions for track lifetime, missing/occlusion gaps and reappearance gaps;
3. case population where nonlinear/multimodal prediction could plausibly change an association decision;
4. matched controls separating generic temporal memory from predictive-belief effects.

Required comparison ladder for the first scientific generation:

```text
Native MOTIP
  -> temporal-memory-only control
  -> deterministic future predictor
  -> fixed-window multimodal predictor
  -> multimodal predictor without MOT feedback
  -> persistent belief + predictive feedback + observation refinement
```

Do not interpret a gain over Native alone as evidence for the MOTPT hypothesis.


## Dataset selection

The canonical dataset plan is `docs/DATASETS.md`.

Current working order:

```text
SportsMOT > DanceTrack > BFT
```

Roles:
- SportsMOT — primary hypothesis/development dataset;
- DanceTrack — secondary mechanism validation/generalization;
- BFT — third extreme-dynamics/domain stress test.

Before G0 dataset freeze, `docs/DATASETS.md` must be updated with independently measured provenance, Native parity, lifetime/gap/reappearance distributions, dynamics statistics, association-opportunity census and detector-bottleneck analysis.
