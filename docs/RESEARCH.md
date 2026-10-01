# MOTPT — Research Contract / Living v0 Formulation

```text
STATUS = V0_CONCEPT_OWNER_ACCEPTED__G0_DISCUSSION_ACTIVE
RESEARCH_HYPOTHESIS = PERSISTENT_OBJECT_SPECIFIC_LATENT_FLOW_BELIEF__WORKING_V0
FORMAL_PROBLEM = WORKING_FORMULATION__NOT_FINAL_G0_FREEZE
ARCHITECTURE = MINIMAL_FOUR_OPERATION_DATAFLOW__NOT_FROZEN
TRAINING_OBJECTIVE = TBD
PROPOSED_MODEL_VERSION = NONE
SCIENTIFIC_EXECUTION = HOLD
```

> **Authority note.** The Project Owner approved this v0 direction for tracked research discussion on 2026-10-01. This document is now the canonical living formulation, but it is **not** the final G0 scientific-contract freeze and does not authorize model implementation or benchmark execution. Definitions, notation, module boundaries, representations and hypotheses may be revised as survey and analysis progress.

## 1. Core research idea

A physical object does not begin or stop moving because a camera observes it. We assume that each object \(i\) participates in an underlying time-evolving dynamical process, denoted conceptually by

\[
F_i(t).
\]

Video provides only discrete and potentially intermittent measurements of that process. At runtime, however, MOT does **not** receive identity-labeled observations. Frame \(t\) provides an unordered observation/detection set

\[
D_t=\{d_t^j\}_{j=1}^{N_t},
\]

and the tracker must infer which observation, if any, corresponds to each persistent object hypothesis.

Detector misses, occlusion, overlap, field-of-view changes and visual ambiguity can make the evidence for a physical object unavailable or unreliable even though the object and its dynamics continue to evolve.

MOTPT therefore studies online multi-object tracking as:

\[
\boxed{\text{sequential inference over persistent object-specific latent-flow beliefs}}
\]

rather than only frame-to-frame detection association.

The model-accessible research object is **not** the unknowable true physical flow itself. Track index \(i\) denotes a **persistent tracker hypothesis**, not a ground-truth identity supplied with the current observation. A working marginal view is

\[
B_t^i \approx p(F_t^i,E_t^i \mid D_{1:t},A_{1:t}),
\]

where \(E_t^i\) denotes existence-related belief and \(A_{1:t}\) is the tracker-inferred association history. The exact joint factorization is intentionally not frozen; association uncertainty may later be represented explicitly rather than conditioned on a single history.

The exact probabilistic representation of \(B_t^i\) is not frozen. Gaussian mixtures, particles, stochastic latent variables, trajectory modes, latent tokens or other calibrated representations remain open.

### Operational emphasis: predictive belief over physical flow

MOTPT keeps both levels:

1. **Underlying flow/process \(F_i(t)\):** the motivating physical/dynamical process that exists independently of whether the camera observes it.
2. **Predictive belief \(B_t^i\):** the model's operational research object—its current uncertain belief about that process and its possible futures.

The first level gives the scientific interpretation; the second is what the model can actually infer, update and evaluate. The project therefore emphasizes **predictive belief more strongly than direct recovery of a “true flow.”** The model belief does not causally change the physical object's motion; instead, current MOT state generates future hypotheses and subsequent observations feed back to revise the belief and tracking decision.

## 2. Bayesian perspective

MOTPT intentionally adopts the **Bayesian filtering / data-assimilation perspective** as a useful abstraction. Bayesian filtering itself is not claimed as novel.

The working loop is:

\[
\boxed{\text{Predict} \rightarrow \text{Observe} \rightarrow \text{Associate} \rightarrow \text{Correct}}
\]

with a learned multimodal MTP component providing a **predictive prior/signal** from the current MOT state back into online MOT.

Conceptually, the current MOT belief/state produces a future distribution

\[
q_t^i(X_{t+1:t+H}) = \mathcal{P}_{\mathrm{MTP}}(B_t^i),
\]

and that predictive distribution contributes evidence for association and state update when the next observations arrive. A generic update can be written as

\[
B_{t+1}^i = \mathcal{U}(B_t^i, q_t^i, D_{t+1}, A_{t+1}).
\]

A closed-form Bayesian update is **not** required. The MTP module is also **not** frozen as the complete latent-state transition operator; its required role is to predict from the current MOT state and return a useful uncertainty-aware signal to MOT.

## 3. Role of MTP: MOT-based future prediction with feedback to MOT

MTP is not the primary task and is not an independent downstream head attached after tracking.

The intended direction is:

\[
\boxed{
\text{current MOT state/belief}
\rightarrow
\text{multimodal MTP prediction}
\rightarrow
\text{predictive signal back to MOT}
}
\]

Given current belief \(B_t^i\), the MTP component models a multimodal predictive distribution such as

\[
q_t^i(X_{t+1:t+H}\mid B_t^i).
\]

This output should have three roles:

1. **Predictive support during weak/missing observation.** Provide plausible future support rather than reducing the track to fixed velocity extrapolation.
2. **Association feedback.** A candidate observation \(z_{t+1}^j\) can be evaluated against the predicted future belief:
   \[
   p(z_{t+1}^j\mid q_t^i,B_t^i).
   \]
3. **Belief refinement signal.** Once an observation is associated, its consistency/inconsistency with prior future hypotheses updates the persistent belief.

MTP therefore acts as a **prediction tool used by MOT**. The primary scientific target remains tracking/identity continuity; forecasting quality is both an auxiliary capability and a diagnostic for whether the predictive belief is meaningful.

## 4. No fixed observation horizon

MOTPT does **not** impose a fixed observation window as part of the scientific problem.

An object's observed lifetime can be arbitrarily long. The intended abstraction is a persistent recursively updated belief:

\[
B_t^i = f(B_{t-1}^i,D_t,A_t),
\]

not an ever-growing raw sequence

\[
[D_1,\ldots,D_t]\rightarrow \text{one unbounded Transformer input}.
\]

The desired property is:

\[
\boxed{\text{unbounded observation lifetime} \rightarrow \text{bounded persistent belief state}}
\]

subject to future empirical validation. Raw-history retention, compression and state capacity remain implementation questions, not assumptions of the problem statement.

### Stage-1 coordinate scope

The first research stage is limited to **2D projected/image-space MOT**. The project does not initially claim recovery of a world-coordinate physical flow. Camera motion, perspective and projection can confound observed trajectories, so the stage-1 object is a **projected predictive flow belief** derived from image-space evidence. Ego-motion compensation or world-relative modeling may be added later only if evidence shows they are necessary.

### Retention/history policy remains empirical

“No fixed observation window” does not mean “retain every raw observation forever” or “keep every disappeared track forever.” The representation may process arbitrarily long track lifetimes through a bounded recursive state, while the computational retention/termination policy remains open.

Before fixing that policy, an authorized dataset diagnostic should measure at least:

- track lifetime distribution;
- visible segment length;
- consecutive missing/occlusion gap distribution;
- reappearance gap distribution;
- frequency of useful identity recovery after different gap lengths.

Those measurements are planned scientific inputs to the retention policy and are **not yet authorized for execution** in the current HOLD state.

## 5. Problems to solve

### P1 — Discrete observations versus persistent dynamics

Standard online MOT primarily operates on observations and recent track history. MOTPT asks whether a persistent latent-flow belief can capture the evolving process that observations only partially reveal.

### P2 — Missing observation versus missing object state

If no usable observation in \(D_t\) is associated with track hypothesis \(i\), that must not automatically imply

\[
B_t^i=\varnothing.
\]

Observation, physical existence, internal belief and externally emitted tracker output are distinct concepts. MOTPT should not require hallucinating an invisible bounding box merely because an internal belief persists.

### P3 — Prediction and identity association are usually separated

If track \(i\) already carries a predictive belief, then a new observation can be tested against it. Prediction should become evidence for identity continuity rather than only a downstream product.

### P4 — Multimodal futures are repeatedly predicted but rarely studied as a persistent revisable belief

For a fixed future target \(T\), MOTPT is interested in the sequence

\[
q_{t_1}(X_T),\quad q_{t_2}(X_T),\quad q_{t_3}(X_T), \qquad t_1<t_2<t_3<T,
\]

where each new valid observation can reweight, prune, split, merge or introduce future modes.

The goal is **future-belief refinement**, not mandatory monotonic entropy reduction. Unexpected motion may correctly increase uncertainty or switch modes.

### P5 — Identity is itself uncertain

Unlike many trajectory-prediction or latent-dynamics settings, MOT must determine which current observation belongs to which persistent object. A working future formulation may therefore need to reason over

\[
p(F_t^i,A_t,E_t^i\mid D_{1:t}),
\]

where \(A_t\) denotes association uncertainty and \(E_t^i\) may represent existence-related belief. The exact factorization is open.

## 6. Minimal proposed dataflow

The v0 design intentionally keeps only four core operations.

### Module / Operation 1 — Observation Encoder

Input may include current detection geometry, appearance/ROI features, detector confidence and causal scene context.

Output:

\[
z_t^j = \operatorname{ObsEnc}(d_t^j).
\]

This represents **what is currently observed**, not the complete object state.

### Module / Operation 2 — Persistent Latent-Flow Belief

Each tracked physical object maintains

\[
B_t^i.
\]

The belief must be capable, directly or indirectly, of representing:

- latent dynamical state;
- uncertainty;
- multimodal future hypotheses;
- information useful for persistent identity.

These are conceptual requirements, not four mandatory neural submodules.

### Module / Operation 3 — MTP Future Predictor / Predictive Signal

\[
B_t^i \xrightarrow{\mathcal{P}_{\mathrm{MTP}}} q_t^i(X_{t+1:t+H}).
\]

The MTP predictor takes the **current MOT belief/state as its base** and produces multimodal future hypotheses plus uncertainty information that can be fed back into MOT.

It is not required in v0 to be the complete hidden-state transition function. It must, however, provide more than deterministic velocity extrapolation or an uncalibrated top-\(K\) coordinate list.

### Module / Operation 4 — Joint Association and Belief Update

At the next frame, candidate observation \(z_{t+1}^j\) is evaluated using both the persistent MOT state and the MTP predictive signal:

\[
p(A_{t+1}^{ij}\mid B_t^i,q_t^i,z_{t+1}^j).
\]

The association mechanism may combine appearance/identity evidence with predictive likelihood or learned flow-belief compatibility.

After association:

\[
B_{t+1}^i = \mathcal{U}(B_t^i,q_t^i,z_{t+1}^j,A_{t+1}^{ij}).
\]

If no usable observation is assigned, the track belief may continue using its previous state plus predictive signal, subject to the future existence/termination policy. That policy is not frozen in v0.

## 7. Working architecture sketch

```text
Current MOT belief B(t)
            |
            +----------------------+
            |                      |
            v                      |
      MTP Future Predictor         |
            |                      |
            v                      |
   multimodal future q(t)          |
            |                      |
            +---- predictive ------+
                  feedback
                     |
next observations -> Observation Encoder
                     |
                     v
             Association / MOT Update
                     |
                     v
                  B(t+1)
                     |
                     +------> next prediction
```

This is a **scientific dataflow sketch**, not an implementation contract.

## 8. Future-belief refinement

MOTPT should evaluate not only whether a future prediction is accurate once, but how belief about the **same future target** changes as additional observations arrive.

For fixed \(T\):

\[
q_t^i(X_T)=p(X_T^i\mid D_{1:t},A_{1:t}).
\]

A useful model should, in expectation and under valid evidence, improve proper predictive scores and calibration as relevant observations accumulate, while retaining the ability to broaden or switch modes after genuinely surprising behavior.

Potential future metrics include proper likelihood scores, calibration, coverage, sharpness, mode recall and refinement curves in addition to ADE/FDE-style trajectory metrics. Exact metrics are not yet frozen.

## 9. Primary research questions

- **RQ1 — Persistent flow:** Can long-lived, discrete and intermittently missing observations support an object-specific latent-flow belief that remains useful over the full track lifetime?
- **RQ2 — Multimodality:** Can that belief represent genuinely unresolved future modes rather than only a deterministic hidden feature?
- **RQ3 — Assimilation:** Do new observations meaningfully revise prior future beliefs through reweighting, pruning, expansion or mode change?
- **RQ4 — Tracking:** Does predictive belief improve identity continuity, especially under occlusion, missed detections, nonlinear motion and ambiguous neighboring objects?
- **RQ5 — MOT-first joint benefit:** Does MTP-derived future belief improve MOT identity continuity, while prediction quality remains measurable enough to validate that the feedback signal is meaningful?
- **RQ6 — Falsifiability:** Can controlled diagnostics show that the learned belief contains information beyond recent velocity/trajectory history or a generic recurrent feature?

## 10. Working contribution hypothesis

If supported empirically, the intended contribution package is:

1. **Persistent latent-flow belief formulation.** Online MOT is framed as sequential inference over object-specific latent dynamical beliefs under discrete/intermittent observations.
2. **MTP-to-MOT predictive feedback.** Learned multimodal trajectory prediction takes the current MOT belief/state as input and returns future uncertainty as an association/update signal, rather than existing only as a downstream forecast.
3. **Observation-conditioned future-belief refinement.** The work explicitly studies how predictions for the same future target evolve as observations accumulate.
4. **MOT-first shared belief.** Identity continuity is the primary task; MTP quality is an auxiliary measurable capability used to validate and improve the same persistent belief process.

These are **working hypotheses/contributions**, not accepted claims.

## 11. Novelty boundary / what MOTPT must not reduce to

The following alone are not claimed as novel:

- Bayesian filtering or data assimilation;
- a recurrent/SSM hidden state;
- object permanence;
- multimodal trajectory forecasting;
- variable observation length;
- joint tracking plus prediction;
- using future prediction to aid tracking;
- an object-centric world model;
- replacing Kalman filtering with a Transformer;
- hallucinating invisible bounding boxes.

The central research burden is to demonstrate that the combination of **persistent object-specific belief + learned multimodal predictive transition + observation-driven posterior refinement + identity inference** forms a meaningful and measurable problem beyond those ingredients individually.

## 12. Minimal falsification-oriented prototype

Before scaling architecture, the first future experimental contract should test whether:

1. under observation dropout, the belief propagates useful uncertainty rather than simply freezing or collapsing;
2. re-observation correctly revises previous multimodal future hypotheses;
3. predictive belief improves identity decisions in controlled ambiguous-association cases;
4. the representation provides information beyond recent-coordinate motion features;
5. gains are jointly visible in tracking and forecasting measures.

Failure on these conditions should trigger problem/method revision rather than automatic architecture expansion.

## 13. Open items before final G0 freeze

Still unresolved:

- formal definition and representational family of latent flow belief;
- whether stage-1 projected/image-space flow requires explicit camera-motion compensation;
- exact existence/termination/retention semantics after dataset-distribution analysis;
- association factorization and role of appearance;
- future horizon and future-mode representation;
- loss functions and probabilistic calibration objective;
- datasets and official splits;
- baseline/checkpoint/config identity;
- evaluation protocol and causal ablations;
- compute budget and implementation scope;
- exact novelty claims after deeper literature review.

No scientific execution is authorized until these are narrowed into a separate explicit G0 freeze.

## 14. Literature survey and novelty tracking

The living nearest-neighbor survey is maintained in [literature/README.md](literature/README.md), with a cross-paper [novelty/collision matrix](literature/NOVELTY_MATRIX.md) and per-paper extraction notes under `docs/literature/papers/`.

The survey is supporting analysis, not accepted scientific evidence. If a literature note conflicts with this research contract, update the contract only through the tracked research workstream rather than silently treating the note as authority.


## 15. Pre-G0 research-value review

The current direction remains scientifically worthwhile **only if** the shared belief formulation survives stronger controls than ordinary motion modeling.

### Value-positive outcome

MOTPT becomes a meaningful contribution if one persistent object belief can simultaneously:

1. represent calibrated multimodal future uncertainty;
2. improve identity association under ambiguity, non-linear motion or missing observations;
3. be corrected by re-observation in a measurable way;
4. improve prediction and tracking through the **same** state rather than independent heads;
5. outperform capacity-matched recurrent/SSM, classical-filter and MTP-only controls for the intended reason.

### Kill / downgrade conditions

The central hypothesis should be revised or downgraded if:

- the proposed belief behaves no better than a deterministic RNN/SSM motion feature;
- tracking gains come only from a stronger predictor but future-belief refinement is not measurable;
- multimodal futures do not improve association or uncertainty calibration;
- the shared state provides no benefit over separate MOT and MTP heads;
- identity-aware assimilation adds complexity without reproducible benefit.

The research value therefore lies in **identity-aware multimodal belief assimilation for online MOT**, not in introducing another motion predictor.


## 16. Owner decisions — 2026-10-01

The following v0 directional decisions are now fixed for the ongoing G0 discussion:

1. **Flow + belief:** both the underlying physical flow/process and model belief remain conceptually relevant, but the operational research emphasis is the **predictive belief**.
2. **MTP role:** MTP takes the current MOT state/belief as its base, predicts multimodal futures, and returns predictive information **back to MOT**.
3. **Terminology:** use **Future Belief Refinement** as the formal term rather than requiring monotonic “future convergence.”
4. **Initial spatial scope:** begin with **2D projected/image-space MOT**; do not initially claim world-flow recovery.
5. **Task priority:** **MOT is primary**. MTP is an auxiliary predictive mechanism and evaluation signal used to improve/validate MOT.
6. **History/retention:** do not freeze a fixed history or track-retention limit yet. First measure dataset track/gap/reappearance distributions under a separately authorized diagnostic, then choose the retention policy.

These decisions narrow the research direction but still do not constitute final G0 architecture/training/evaluation freeze.


### Critical nearest-neighbor update — DiffuTrack

A 2026 online MOT work, **DiffuTrack**, already uses conditional diffusion to generate distributional/multimodal motion hypotheses from track history and feeds those hypotheses directly into data association. This materially tightens the novelty boundary.

Therefore MOTPT must **not** claim the following as sufficient novelty:

- probabilistic/multimodal motion prediction for MOT;
- multiple future hypotheses instead of one Kalman/point prediction;
- future-distribution support used for association.

The remaining research burden is stronger: the project must demonstrate a **persistent longitudinal belief** that is observation-updated across the track lifetime, whose belief about the **same future target** can be measured as it refines, and whose persistent identity state is coupled to that refinement.

A fixed-window multimodal motion predictor without those properties should be treated as a baseline/control, not the final MOTPT contribution.


### Pre-experiment feasibility verdict

**Status: CONDITIONAL GO.**

The project is technically feasible and MOTIP has demonstrated headroom for temporal/association improvements, but the first experiment must be designed to distinguish MOTPT from simpler explanations.

The experiment is considered informative only if it can separate:

- extra temporal memory;
- deterministic learned motion prediction;
- fresh fixed-window multimodal motion hypotheses;
- prediction used only as an auxiliary output;
- the target MOTPT mechanism: **persistent belief + predictive feedback + observation-driven same-future refinement**.

A gain over Native MOTIP alone is insufficient, because recent work already shows that generic temporal fusion, discriminative temporal embeddings and distributional motion hypotheses can improve tracking.


## 17. Model generation and validation-iteration policy

MOTPT is expected to require multiple model generations and multiple validation rounds. These identities must be planned explicitly so scientific changes are not confused with tuning/debug runs.

### 17.1 Four-level identity

```text
Model Generation  = M#
Validation Iteration = V##
Execution Run = R####
Evidence Question = E###
```

These levels have different meanings.

### Model Generation — `M#`

A new `M#` is created **only for a material scientific change**.

Examples that require a new model generation:

- changing model-visible information or causal boundary;
- changing the semantic belief representation family;
- adding/removing a core module or feedback path;
- changing MTP from one scientific role to another;
- adding/removing supervision or a loss term that changes the scientific objective;
- changing observation-assimilation semantics;
- changing identity/existence factorization in a way that changes the hypothesis being tested.

Examples that do **not** by themselves create a new model generation:

- seed;
- learning rate;
- batch size;
- hidden dimension;
- number of epochs;
- checkpoint choice within the same contract;
- logging;
- bug fix that restores the frozen contract;
- evaluator-only diagnostics;
- prediction horizon or retention threshold explored under the same model semantics;
- changing a loss weight while retaining the same objective terms.

### Validation Iteration — `V##`

A validation iteration is a **promoted configuration/evaluation round within one model generation**.

Use a new `V##` when the scientific model is unchanged but a configuration is intentionally promoted for comparison, for example:

- candidate prediction horizon;
- number of future modes;
- belief capacity;
- retention threshold;
- calibrated feedback strength;
- optimizer/training schedule selected for an endpoint comparison;
- a revised but semantically identical training recipe.

Do **not** create a new `V##` for every debug/tuning run. Exploratory runs remain ordinary `R####` executions until a configuration is promoted.

### Execution Run — `R####`

Every actual execution gets an immutable run identity.

A run binds at least:

- `M#`;
- optional `V##`;
- code Git SHA;
- config hash;
- checkpoint/input hashes;
- dataset/split/population;
- seed;
- evaluator;
- output artifact reference/hash.

Repeated seeds and reruns are separate `R####`, not new model versions.

### Evidence Question — `E###`

`E###` lives only in `docs/EVIDENCE.md` and represents a scientific question/adjudicated comparison.

Multiple model generations, validation iterations and runs can contribute to one evidence entry.

Example:

```text
E003 — Does persistent predictive belief improve association after re-observation?

  B0 / R0041
  C2 / R0042-R0044
  C3 / R0045-R0047
  M1-V02 / R0050-R0054
```

The evidence identity must not equal the run identity.

### 17.2 Baseline and control identities

Baseline/control variants use separate namespaces and do not consume MOTPT model-generation numbers:

```text
B0 = Native MOTIP

C1 = Temporal-memory-only control
C2 = Deterministic future predictor
C3 = Fixed-window multimodal predictor
C4 = Multimodal prediction without MOT feedback
```

The first target MOTPT scientific generation is reserved as:

```text
M1 = Persistent predictive belief
     + multimodal MTP prediction
     + predictive feedback to MOT
     + observation-driven belief refinement
```

`M1` is **reserved, not implemented or accepted**. Its exact representation/loss remains subject to final G0 freeze.

Do not pre-name `M2`, `M3`, etc. A later generation exists only after evidence motivates a material scientific change.

### 17.3 Promotion rule

The normal lifecycle is:

```text
idea / debug runs
    -> promoted V## within current M#
    -> controlled primary-dataset evaluation
    -> falsification / matched controls
    -> secondary-dataset validation
    -> evidence adjudication
    -> ACCEPT / REVISE / KILL
```

A poor result does **not** automatically justify a new model generation.

Before creating `M(n+1)`, state:

1. what evidence falsified or limited `Mn`;
2. what scientific mechanism changes;
3. why the change cannot be represented as another `V##`;
4. which prior controls must be rerun;
5. which evidence entry will adjudicate the new generation.

### 17.4 Git is provenance, not model identity

Do not use branch names, commit numbers, checkpoint filenames or Markdown copies as the model-version system.

Correct:

```text
M1-V02 / R0051
code_sha = <git SHA>
config_hash = <hash>
checkpoint_hash = <hash>
```

Incorrect:

```text
model_final_v3_new
branch_m1_fix2
checkpoint_best_latest
MOTPT_v7_really_final
```

Git records implementation history. `M# / V## / R#### / E###` records scientific identity.

### 17.5 Planned validation ladder

The validation ladder should be reusable across model generations:

```text
Stage 0 — static / synthetic contract tests
Stage 1 — baseline parity + dataset/opportunity diagnostics
Stage 2 — primary-dataset canary
Stage 3 — primary endpoint + matched controls
Stage 4 — mechanism/falsification slices
Stage 5 — DanceTrack independent validation
Stage 6 — BFT stress test
```

Not every candidate reaches every stage. A generation can be stopped early if the mechanism fails.
