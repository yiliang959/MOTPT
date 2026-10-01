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
CURRENT_TASK = REFINE_PROBLEM_NOVELTY_MODULES_AND_G0_REQUIREMENTS
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
persistent object belief
    -> MTP predictive transition
    -> current observation
    -> predictive association
    -> belief correction
    -> next frame
```

MTP is treated as a predictive tool **inside** MOT. MOTPT does not impose a fixed observation window; each object's belief is recursively maintained across its tracked lifetime.

## Current scientific status

The formulation in `docs/RESEARCH.md` is accepted as the canonical **working concept**, not a final method or validated claim.

No dataset, model implementation, training objective, evaluation population or acceptance threshold is yet frozen. `docs/EVIDENCE.md` remains empty of accepted MOTPT scientific results.

## Next decisions before G0 freeze

1. tighten the mathematical definition of latent-flow belief and its uncertainty/multimodality semantics;
2. convert the survey into explicit novelty/non-novelty boundaries and nearest-neighbor comparisons;
3. define minimal falsification tests and baselines;
4. decide image-space versus world-relative/camera-compensated flow assumptions;
5. select datasets/splits, MTP representation family and MOTIP integration point;
6. freeze one minimal implementable contract before any scientific execution.

Until then, literature review, docs/governance edits and synthetic/static tests are allowed; benchmark-consuming research execution is not.
