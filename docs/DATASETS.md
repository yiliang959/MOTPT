# MOTPT — Dataset Selection and Verification

```text
STATUS = WORKING_SELECTION__NOT_G0_FROZEN
CURRENT_ORDER = SportsMOT > DanceTrack > BFT
PRIMARY_HYPOTHESIS_DATASET = SportsMOT
SECONDARY_VALIDATION_DATASET = DanceTrack
THIRD_STRESS_TEST_DATASET = BFT
DATASET_EXECUTION = HOLD__NO_DATASET_CONSUMING_ANALYSIS_YET
UPDATE_POLICY = IN_PLACE_ONLY
```

## 1. Purpose

This is the **single canonical dataset document** for MOTPT.

It records:

- why each candidate dataset is scientifically useful;
- the current working order and intended role;
- what must be measured before the dataset/split contract is frozen;
- which observations would change the current ranking;
- the checklist that must be revisited as experiments progress.

Do not create `DATASETS_v2.md`, per-dataset planning files, or dated dataset-selection snapshots. Update this document in place; Git already preserves history.

The current order is a **working research decision**, not accepted evidence. All dataset statistics used for scientific decisions must be independently reproduced from the exact local dataset/split before final G0 freeze.

---

## 2. Current working decision

[
oxed{	ext{SportsMOT} > 	ext{DanceTrack} > 	ext{BFT}}
]

Recommended experimental roles:

| Dataset | MOTPT suitability | Working role | Main reason |
|---|---:|---|---|
| **SportsMOT** | Highest | Primary hypothesis / development dataset | long-lived identities, rapid/nonlinear motion, frequent interactions, similar appearance, meaningful observation gaps and reappearance |
| **DanceTrack** | High | Secondary validation / generalization | uniform appearance and diverse motion make identity association depend strongly on temporal/motion reasoning |
| **BFT** | Medium–High, highest confounding risk | Third stress test / extreme-domain validation | highly dynamic small/deforming targets and strong projection/occlusion effects provide a hard generalization test |

If only one dataset can be used initially: **SportsMOT**.

If two are needed for the first credible scientific result: **SportsMOT + DanceTrack**.

BFT should normally be added after the core mechanism has been validated, because failure on BFT is harder to attribute specifically to predictive-belief quality.

---

## 3. Why SportsMOT is the primary dataset

SportsMOT is currently the cleanest fit to the MOTPT hypothesis.

The target mechanism needs situations where:

[
	ext{persistent identity}
+
	ext{nonlinear future}
+
	ext{temporary observation uncertainty}
+
	ext{reappearance}
]

can affect association.

Sports scenes naturally contain:

- long-lived player identities;
- acceleration, deceleration and turning;
- visually similar objects in close proximity;
- repeated crossings and interaction;
- short and long observation gaps;
- camera motion;
- association ambiguity that cannot always be solved by appearance alone.

This makes SportsMOT suitable for testing whether a persistent future belief adds information beyond:

- recent velocity;
- generic temporal memory;
- deterministic learned prediction;
- fresh fixed-window multimodal hypotheses.

### Working expectation

The main expected gain should be in:

- AssA;
- ID continuity / IDSW;
- re-association after observation gaps;
- nonlinear-motion and ambiguous-neighbor cases.

A gain dominated only by DetA would not strongly support the MOTPT hypothesis.

### Sports-level decomposition

Basketball, volleyball and football should not automatically be pooled for all diagnostics.

Before choosing MTP horizon or retention policy, compare their:

- track lifetime distributions;
- observation-gap distributions;
- reappearance-gap distributions;
- velocity / acceleration / turning statistics;
- camera-motion characteristics;
- object density and association ambiguity.

The sub-sport distributions may imply different useful predictive horizons.

---

## 4. Why DanceTrack is the second dataset

DanceTrack was designed around **uniform appearance and diverse motion**, which makes it highly relevant to MOTPT.

It is valuable because:

- appearance is intentionally less discriminative;
- trajectories contain crossing, relative-position exchange and nonlinear motion;
- association quality is a central difficulty;
- success would show that the method is not sports-specific.

### Why it is not the first development dataset

DanceTrack combines several effects:

- choreography and highly coordinated motion;
- body articulation;
- crossover;
- camera/image-space effects;
- potentially difficult 2D future prediction.

If an early model fails on DanceTrack, it may be unclear whether the research hypothesis failed or the stage-1 projected future representation is simply too difficult.

Therefore DanceTrack is currently better used as the **second mechanism-validation/generalization dataset** after the core predictive-belief loop has shown evidence on SportsMOT.

---

## 5. Why BFT is the third dataset

BFT is scientifically interesting because bird tracking contains extreme dynamics, including:

- fast motion;
- strong shape/deformation changes;
- flock interaction and occlusion;
- small targets;
- 3D activity projected into 2D;
- highly uncertain short-term motion.

These properties make BFT a useful stress test of whether the learned belief generalizes beyond human sports motion.

### Main confounding risk

BFT errors may simultaneously come from:

[
	ext{localization}
+
	ext{small-target detection}
+
	ext{deformation}
+
	ext{3D projection}
+
	ext{occlusion}
+
	ext{association}.
]

Therefore a negative BFT result does not cleanly falsify MOTPT unless the detector/localization bottleneck and available association opportunity are first quantified.

BFT should be used after SportsMOT/DanceTrack establish that the mechanism can work under a more interpretable association regime.

---

## 6. Dataset-selection falsification logic

The current order should be revised if the measured data contradicts the working assumptions.

### SportsMOT should be downgraded if

- useful observation/reappearance gaps are rare under the exact split used;
- most Native errors are detector/localization failures rather than association failures;
- nonlinear/multimodal prediction almost never changes the plausible association set;
- camera motion dominates the image-space dynamics to the point that projected prediction is not informative.

### DanceTrack should move to primary if

- it contains substantially more prediction-sensitive association events than SportsMOT;
- Native MOTIP's dominant correctable error population is clearly association/motion-driven;
- SportsMOT gains are mostly sport-specific or appearance/context-driven.

### BFT should move earlier only if

- detector/localization quality is sufficient to expose a sizable association-error population;
- projected motion belief remains meaningfully predictable despite 3D projection and deformation;
- BFT provides uniquely strong evidence for multimodal future refinement rather than mostly detection difficulty.

---

# 7. Mandatory verification checklist before G0 dataset freeze

All items below must be reviewed and this file updated in place.

## A. Dataset provenance and split identity

### SportsMOT
- [ ] Verify official source/repository/version.
- [ ] Verify exact train/val/test split.
- [ ] Verify sequence count and frame-rate assumptions.
- [ ] Verify local annotation format and any conversion.
- [ ] Record dataset/input hash or immutable local manifest.
- [ ] Confirm whether any val data enters training.
- [ ] Confirm detector inputs are identical across baseline/ours.

### DanceTrack
- [ ] Verify official source/repository/version.
- [ ] Verify exact train/val/test split.
- [ ] Verify local annotation format and any conversion.
- [ ] Record immutable local manifest.
- [ ] Confirm whether any val data enters training.
- [ ] Confirm detector inputs are identical across baseline/ours.

### BFT
- [ ] Verify official source/repository/version.
- [ ] Verify exact train/val/test split.
- [ ] Verify local annotation format and any conversion.
- [ ] Record immutable local manifest.
- [ ] Confirm whether any val data enters training.
- [ ] Confirm detector inputs are identical across baseline/ours.

---

## B. Native MOTIP parity

For each candidate dataset:

- [ ] Pin exact MOTIP source SHA.
- [ ] Pin config.
- [ ] Pin checkpoint hash.
- [ ] Pin detector/detection input.
- [ ] Pin evaluator / TrackEval version.
- [ ] Reproduce Native output.
- [ ] Record HOTA / DetA / AssA / ID-related metrics.
- [ ] Quantify run-to-run variance if training is required.
- [ ] Decide the parity tolerance before evaluating MOTPT changes.

No MOTPT gain is interpretable until baseline parity is established.

---

## C. Track lifetime / observation structure

Measure separately for train and the evaluation population:

- [ ] track lifetime distribution;
- [ ] visible contiguous segment length;
- [ ] number of gaps per identity;
- [ ] consecutive missing/occlusion gap length;
- [ ] reappearance gap length;
- [ ] fraction of identities reappearing after 1/2/4/8/16/32/... frames;
- [ ] sequence-level and category/sport-level variation;
- [ ] density of simultaneous active objects.

These measurements determine whether a persistent belief and long retention policy have a meaningful target population.

---

## D. Dynamics / multimodality opportunity

Measure:

- [ ] displacement distribution;
- [ ] speed distribution;
- [ ] acceleration/deceleration;
- [ ] heading/turn-angle change;
- [ ] trajectory curvature;
- [ ] abrupt maneuver frequency;
- [ ] candidate future multimodality proxy;
- [ ] camera-motion magnitude / scene-motion proxy;
- [ ] difference across SportsMOT sports / DanceTrack sequences / BFT scenes.

The goal is not only to show motion is “hard,” but to estimate where **multiple plausible futures** exist and where new observations could refine them.

---

## E. Association-opportunity census

This is one of the most important pre-model analyses.

For Native MOTIP failures and ambiguous frames, estimate:

- [ ] number of plausible detections per active track;
- [ ] number of active tracks competing for the same observation;
- [ ] appearance ambiguity;
- [ ] motion ambiguity;
- [ ] cases where deterministic prediction selects the wrong candidate;
- [ ] cases where a broader/multimodal prediction would retain the correct candidate;
- [ ] cases where future prediction cannot help because the correct detection is absent;
- [ ] cases dominated by detector/localization error;
- [ ] gap/reappearance cases where persistent belief could change the decision.

This defines the **upper-bound opportunity population** for MOTPT.

---

## F. Detector / localization bottleneck check

For every dataset:

- [ ] estimate FN / FP contribution;
- [ ] estimate association-error contribution;
- [ ] check whether GT exists but detector candidate is missing;
- [ ] inspect localization quality under fast motion / deformation;
- [ ] identify cases where prediction cannot recover because no usable observation exists;
- [ ] decide whether the dataset is suitable for testing association rather than detector quality.

A dataset with poor detection but little association opportunity is a weak primary benchmark for MOTPT.

---

## G. MTP horizon and belief-retention implications

After the distributions are measured:

- [ ] choose candidate prediction horizons (H);
- [ ] choose short/medium/long reappearance-gap buckets;
- [ ] determine whether one horizon is sufficient;
- [ ] determine whether sport/scene-specific horizons are needed for analysis;
- [ ] decide bounded belief-state capacity;
- [ ] decide track-retention / termination policy;
- [ ] confirm that no fixed raw-history window is being silently introduced;
- [ ] quantify computational cost as track lifetime grows.

Do **not** choose horizon or retention only because it is conventional in MTP literature.

---

## H. Matched baseline / control availability

For each dataset confirm feasibility of:

- [ ] Native MOTIP;
- [ ] temporal-memory-only control;
- [ ] deterministic learned predictor;
- [ ] fixed-window multimodal predictor;
- [ ] prediction without feedback to MOT;
- [ ] persistent belief + feedback + observation refinement.

If a control cannot be implemented fairly on a dataset, document the limitation before interpreting gains.

---

## I. Evaluation plan

Primary MOT measures:
- [ ] HOTA;
- [ ] AssA;
- [ ] DetA;
- [ ] IDF1 / ID-related metrics as appropriate;
- [ ] IDSW;
- [ ] fragmentation / re-association diagnostics.

Secondary predictive-belief measures:
- [ ] ADE/FDE-style metrics where meaningful;
- [ ] NLL or another proper score if tractable;
- [ ] coverage;
- [ ] calibration;
- [ ] sharpness;
- [ ] mode recall/diversity;
- [ ] same-future refinement curve (q_t(X_T)).

Mechanism slices:
- [ ] nonlinear motion;
- [ ] short gap;
- [ ] long gap;
- [ ] reappearance;
- [ ] high-density / ambiguous neighbors;
- [ ] similar appearance;
- [ ] camera-motion-heavy cases.

---

# 8. Working experimental order

Unless the checklist produces contrary evidence:

```text
Phase 0:
    SportsMOT + DanceTrack + BFT
    -> cheap dataset/provenance/distribution/opportunity analysis

Phase 1:
    SportsMOT
    -> Native parity
    -> minimal falsification controls
    -> first persistent-belief prototype

Phase 2:
    DanceTrack
    -> independent mechanism validation / generalization

Phase 3:
    BFT
    -> extreme dynamics / projection / domain stress test
```

Do not begin three full training programs simultaneously.

---

# 9. Decision log — current state

## Working decision

- **Primary:** SportsMOT.
- **Secondary:** DanceTrack.
- **Stress test:** BFT.
- **MOT is the primary task; MTP is auxiliary predictive feedback.**
- No dataset/split is formally G0-frozen yet.
- Dataset-consuming analysis remains prohibited until separately authorized.

## Why SportsMOT first

SportsMOT currently offers the cleanest combination of:

[
	ext{long-lived identity}
+
	ext{rapid/nonlinear motion}
+
	ext{similar appearance}
+
	ext{observation gap}
+
	ext{association ambiguity}.
]

That is the closest match to the first MOTPT falsification question:

> Does a persistent, observation-updated predictive belief improve identity continuity beyond generic memory and fresh motion prediction?

---

# 10. External references to verify against local data

These sources motivate the current working order, but **local statistics must replace source-level assumptions before G0 freeze**.

- SportsMOT official repository: https://github.com/MCG-NJU/SportsMOT
- DanceTrack paper: https://openaccess.thecvf.com/content/CVPR2022/html/Sun_DanceTrack_Multi-Object_Tracking_in_Uniform_Appearance_and_Diverse_Motion_CVPR_2022_paper.html
- BFT / NetTrack paper: https://openaccess.thecvf.com/content/CVPR2024/html/Zheng_NetTrack_Tracking_Highly_Dynamic_Objects_with_a_Net_CVPR_2024_paper.html
- MOTIP: https://github.com/MCG-NJU/MOTIP

When any verification changes the dataset ranking, update this document and the dataset field in `governance.json` / `docs/CURRENT.md` in the same tracked workstream.
