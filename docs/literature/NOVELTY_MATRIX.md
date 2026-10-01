# MOTPT Novelty / Collision Matrix

- **✓** = explicit/central in the surveyed work.
- **~** = related/partial.
- **—** = not central.
- These cells are working literature judgments, not claims by the original authors.

| Work | Persistent state | Partial / missing obs | Multimodal future | Sequential future correction | MOT identity association | Joint tracking + prediction | Main overlap |
|---|:---:|:---:|:---:|:---:|:---:|:---:|---|
| LG-ODE (NeurIPS'20) | ✓ | ✓ | ~ | ~ | — | — | latent dynamics from partial observations |
| Object Permanence (ECCV'20) | ✓ | ✓ | — | ~ | — | — | unseen object state |
| PnPNet (CVPR'20) | ✓ | ~ | ~ | — | ✓ | ✓ | tracking in perception/forecast loop |
| PermaTrack (ICCV'21) | ✓ | ✓ | — | ~ | ✓ | ~ | recurrent tracking through occlusion |
| Random Walk Memory (ICML'22) | ✓ | ✓ | — | ~ | ~ | — | self-supervised persistent memory |
| Loci (ICLR'23) | ✓ | ✓ | ~ | ~ | ~ | ~ | identity/location latent dynamics |
| SlotFormer (ICLR'23) | ✓ | ~ | ~ | — | — | — | object-centric future dynamics |
| PF-Track (CVPR'23) | ✓ | ✓ | ~ | — | ✓ | ✓ | future motion aids re-association |
| FLN (CVPR'24) | ~ | ~ | model-dependent | — | — | — | variable observation length |
| DriveWorld (CVPR'24) | ✓ | ~ | ~ | ~ | downstream | ✓ | latent dynamics for MOT + forecast |
| StreamMOTP (ACCV'24) | ✓ | ~ | ~ | ~ | ✓ | ✓ | streaming joint MOT + MTP |
| CLLS (CVPR'25) | ✓ | ~ | model-dependent | — | — | — | length-robust recurrent representation |
| TOTP (ICCV'25) | ✓ | ~ | ✓ | ~ | — | — | online variable-observation MTP |
| DreamTrack (CVPR'25) | ✓ | ~ | ✓ | ~ | SOT | ✓ (SOT) | multimodal future aids tracking |
| HyperSSM (CVPR'26) | ✓ | ✓ | — | — | ✓ | ~ | learned state-space MOT motion |
| Bayes-4DRTrack (IV'25) | ✓ | ~ | uncertainty-aware | ~ | ✓ | ✓ | Transformer motion prediction + Bayesian uncertainty in MOT |
| LPWM (ICLR'26) | ✓ | ~ | ✓ | ~ | — | — | object-centric stochastic dynamics |
| SURGE (ICML'26) | ✓ | ✓ | ✓ | ✓ | — | — | observation-corrected forecast posterior |
| IMSETrack (ESWA'26) | ✓ | ✓ | — | ~ | SOT | ~ | persistent implicit motion state |
| Sentinel (Sci. Rep.'26) | ✓ | ✓ | — | — | ✓ | — | per-track uncertainty-aware association/lifecycle |
| **MOTPT target** | **✓** | **✓** | **✓** | **✓ core** | **✓ core** | **✓ same belief** | identity-aware posterior over latent flow |

## Claims this matrix rules out

Do **not** base MOTPT novelty solely on:
- unseen objects keeping internal state;
- RNN/SSM/latent motion state;
- long or variable observation history;
- multimodal trajectory prediction;
- prediction improving tracking;
- joint MOT + MTP training;
- object-centric latent dynamics;
- observations correcting a predicted latent state.

## Stronger working distinction

\[
\boxed{
\text{latent dynamics}
+
\text{future multimodality}
+
\text{observation assimilation}
+
\text{object identity}
}
\]

The four parts should not be independent heads. One persistent belief should predict futures, constrain association, be corrected by the associated observation, and expose how belief about the **same future event** evolves.

## Highest-risk nearest neighbors

- **SURGE:** closest prediction/correction semantics; MOTPT must add ambiguous identity association.
- **StreamMOTP:** closest streaming joint MOT + MTP; MOTPT needs explicit belief semantics and posterior revision.
- **PF-Track:** closest future-prediction-to-reassociation mechanism.
- **TOTP:** closest online multimodal MTP with variable observations; lacks MOT identity inference.
- **LPWM:** closest object-centric stochastic latent dynamics; lacks standard MOT association focus.
- **HyperSSM / IMSETrack:** strongest warning against renaming a recurrent/SSM hidden state as latent flow.
- **Bayes-4DRTrack:** blocks a novelty claim based only on learned nonlinear motion prediction + Bayesian uncertainty inside MOT.
- **Sentinel:** blocks a novelty claim based only on per-track uncertainty state driving association/lifecycle.

## Experiments implied by the literature

- capacity-matched RNN/SSM hidden-state control;
- Kalman/Bayesian-style motion control where appropriate;
- MTP-only predictor whose future does not feed association;
- MOT + MTP independent/joint heads without posterior semantics;
- controlled observation-dropout duration;
- re-observation mode reweight/prune test;
- abrupt behavior change / belief expansion test;
- same-future refinement curve for \(q_t(X_T)\);
- ambiguous-association test with similar objects but divergent dynamics.
