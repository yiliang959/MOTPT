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

Video provides only discrete and potentially intermittent observations of that process:

\[
O_t^i.
\]

Detector misses, occlusion, overlap, field-of-view changes and visual ambiguity can make \(O_t^i\) unavailable or unreliable even though the physical object and its dynamics continue to evolve.

MOTPT therefore studies online multi-object tracking as:

\[
\boxed{\text{sequential inference over persistent object-specific latent-flow beliefs}}
\]

rather than only frame-to-frame detection association.

The model-accessible research object is **not** the unknowable true physical flow itself. It is a belief over latent flow conditioned on causal observations:

\[
B_t^i = p(F_t^i \mid O_{\le t}).
\]

The exact probabilistic representation of \(B_t^i\) is not frozen. Gaussian mixtures, particles, stochastic latent variables, trajectory modes, latent tokens or other calibrated representations remain open.

## 2. Bayesian perspective

MOTPT intentionally adopts the **Bayesian filtering / data-assimilation perspective** as a useful abstraction. Bayesian filtering itself is not claimed as novel.

The working loop is:

\[
\boxed{\text{Predict} \rightarrow \text{Observe} \rightarrow \text{Associate} \rightarrow \text{Correct}}
\]

with a learned multimodal MTP component serving as the predictive/transition mechanism inside online MOT.

Conceptually:

\[
B_{t|t-1}^i = \mathcal{P}(B_{t-1}^i)
\]

followed by association against current observations, and for an accepted observation \(z_t^j\),

\[
B_t^i = \mathcal{U}(B_{t|t-1}^i,z_t^j).
\]

A closed-form Bayesian update is **not** required. The learned operators may approximate prediction and posterior correction while preserving explicit uncertainty semantics.

## 3. Role of MTP: predictive operator inside MOT

MTP is not an independent downstream head attached after tracking.

Given current belief \(B_t^i\), the MTP component models a multimodal predictive distribution such as

\[
q_t^i(X_{t+1:t+H}\mid B_t^i).
\]

This predictive belief should have three roles:

1. **Propagation.** When no usable observation is available, maintain and evolve the object's belief rather than equating missing observation with missing state.
2. **Association evidence.** A candidate observation \(z_t^j\) should be evaluated partly under the predictive belief of object \(i\):
   \[
   p(z_t^j\mid B_{t|t-1}^i).
   \]
3. **Future prediction.** Expose the current multimodal future belief as an explicit prediction product that can be evaluated and later revised.

The intended research distinction is therefore:

\[
\boxed{\text{MTP-as-transition/predictive inference for MOT, not MOT + an auxiliary MTP head}}
\]

## 4. No fixed observation horizon

MOTPT does **not** impose a fixed observation window as part of the scientific problem.

An object's observed lifetime can be arbitrarily long. The intended abstraction is a persistent recursively updated belief:

\[
B_t^i = f(B_{t-1}^i,O_t),
\]

not an ever-growing raw sequence

\[
[O_1,\ldots,O_t]\rightarrow \text{one unbounded Transformer input}.
\]

The desired property is:

\[
\boxed{\text{unbounded observation lifetime} \rightarrow \text{bounded persistent belief state}}
\]

subject to future empirical validation. Raw-history retention, compression and state capacity remain implementation questions, not assumptions of the problem statement.

## 5. Problems to solve

### P1 — Discrete observations versus persistent dynamics

Standard online MOT primarily operates on observations and recent track history. MOTPT asks whether a persistent latent-flow belief can capture the evolving process that observations only partially reveal.

### P2 — Missing observation versus missing object state

\[
O_t^i=\varnothing
\]

must not automatically imply

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
p(F_t^i,A_t,E_t^i\mid O_{\le t}),
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

### Module / Operation 3 — MTP Predictive Transition

\[
B_{t-1}^i \xrightarrow{\mathcal{P}} B_{t|t-1}^i
\]

and

\[
B_t^i \rightarrow q_t^i(X_{t+1:t+H}).
\]

The transition should support uncertainty evolution and multimodal futures. It should not be reduced by definition to deterministic velocity extrapolation or top-\(K\) coordinate regression.

### Module / Operation 4 — Joint Association and Belief Update

For current observation \(z_t^j\), estimate association compatibility:

\[
p(A_t^{ij}\mid B_{t|t-1}^i,z_t^j).
\]

The association mechanism may combine appearance/identity evidence with predictive likelihood or learned flow-belief compatibility.

After association:

\[
B_t^i = \mathcal{U}(B_{t|t-1}^i,z_t^j).
\]

If no usable observation is assigned, the predicted belief can persist subject to future existence/termination policy. That policy is not frozen in v0.

## 7. Working architecture sketch

```text
Persistent object belief B(t-1)
            |
            v
   MTP Predict / Transition
            |
            +------------------> multimodal future belief
            |
            v
    predicted belief B(t|t-1)
            |
current observations -> Observation Encoder
            |                    |
            +------> Association-+
                         |
                         v
                  Belief Correction
                         |
                         v
                        B(t)
                         |
                         +------> next frame
```

This is a **scientific dataflow sketch**, not an implementation contract.

## 8. Future-belief refinement

MOTPT should evaluate not only whether a future prediction is accurate once, but how belief about the **same future target** changes as additional observations arrive.

For fixed \(T\):

\[
q_t(X_T)=p(X_T\mid O_{\le t}).
\]

A useful model should, in expectation and under valid evidence, improve proper predictive scores and calibration as relevant observations accumulate, while retaining the ability to broaden or switch modes after genuinely surprising behavior.

Potential future metrics include proper likelihood scores, calibration, coverage, sharpness, mode recall and refinement curves in addition to ADE/FDE-style trajectory metrics. Exact metrics are not yet frozen.

## 9. Primary research questions

- **RQ1 — Persistent flow:** Can long-lived, discrete and intermittently missing observations support an object-specific latent-flow belief that remains useful over the full track lifetime?
- **RQ2 — Multimodality:** Can that belief represent genuinely unresolved future modes rather than only a deterministic hidden feature?
- **RQ3 — Assimilation:** Do new observations meaningfully revise prior future beliefs through reweighting, pruning, expansion or mode change?
- **RQ4 — Tracking:** Does predictive belief improve identity continuity, especially under occlusion, missed detections, nonlinear motion and ambiguous neighboring objects?
- **RQ5 — Joint benefit:** Do tracking and future prediction improve through a shared latent-flow belief rather than two loosely coupled heads?
- **RQ6 — Falsifiability:** Can controlled diagnostics show that the learned belief contains information beyond recent velocity/trajectory history or a generic recurrent feature?

## 10. Working contribution hypothesis

If supported empirically, the intended contribution package is:

1. **Persistent latent-flow belief formulation.** Online MOT is framed as sequential inference over object-specific latent dynamical beliefs under discrete/intermittent observations.
2. **MTP as the MOT predictive operator.** Learned multimodal trajectory prediction becomes the transition/predictive mechanism used for propagation and identity association, not merely an auxiliary forecasting task.
3. **Observation-conditioned future-belief refinement.** The work explicitly studies how predictions for the same future target evolve as observations accumulate.
4. **Unified tracking and prediction state.** Identity continuity and multimodal future prediction use one persistent belief process.

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
- treatment of camera motion and image-space versus world-relative dynamics;
- exact existence/termination semantics;
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
