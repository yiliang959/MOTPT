# MOTPT Literature Survey

**Last verified:** 2026-10-01  
**Status:** living survey for Issue #1 / Draft PR #2  
**Role:** supporting novelty analysis; it does not override `docs/RESEARCH.md` or `docs/EVIDENCE.md`.

## Purpose

This directory records papers most likely to overlap with, be confused with, or materially inform MOTPT. The goal is not paper count. Every note asks:

> **What has already been solved, what can MOTPT reuse, and what must MOTPT do differently?**

Current MOTPT target: a persistent object-specific latent-flow **belief** in online MOT, with MTP as its predictive transition operator, predictive belief participating in association, and later observations revising multimodal future belief.

## Taxonomy

| Family | Established prior art | Not sufficient as MOTPT novelty |
|---|---|---|
| Bayesian filtering / data assimilation | predict → observe → posterior correction | sequential posterior updating |
| Partial-observation latent dynamics | infer latent dynamics from incomplete samples | hidden continuous dynamics |
| Object permanence | object state can persist without visibility | “unseen object still exists” |
| Recurrent / SSM tracking | learned persistent motion state improves tracking | hidden motion state |
| Joint MOT + MTP | tracking and prediction can be unified | “we combine MOT and MTP” |
| Variable-observation MTP | prediction can accept changing history lengths | no fixed observation window |
| Multimodal forecasting | future can be represented by modes/samples | K predicted trajectories |
| Object-centric world models | stochastic per-object latent dynamics can be learned | object-centric latent dynamics |
| **MOTPT target intersection** | not found as one standard formulation in this survey | persistent belief + MTP transition + correction + uncertain identity |

## Paper index

### Partial observations / Bayesian-like inference
- [LG-ODE — NeurIPS 2020](papers/2020_neurips_lg_ode.md)
- [SURGE — ICML 2026](papers/2026_icml_surge.md)

### Object permanence / persistent state
- [Learning Object Permanence from Video — ECCV 2020](papers/2020_eccv_object_permanence_video.md)
- [Learning To Track With Object Permanence — ICCV 2021](papers/2021_iccv_permatrack.md)
- [Random Walk along Memory — ICML 2022](papers/2022_icml_object_permanence_memory.md)
- [Loci — ICLR 2023](papers/2023_iclr_loci.md)
- [IMSETrack — ESWA 2026](papers/2026_eswa_imsetrack.md)

### Joint tracking + future prediction
- [PnPNet — CVPR 2020](papers/2020_cvpr_pnpnet.md)
- [PF-Track — CVPR 2023](papers/2023_cvpr_pf_track.md)
- [StreamMOTP — ACCV 2024](papers/2024_accv_streammotp.md)
- [DreamTrack — CVPR 2025](papers/2025_cvpr_dreamtrack.md)

### Online / variable-observation MTP
- [FLN — CVPR 2024](papers/2024_cvpr_fln.md)
- [CLLS — CVPR 2025](papers/2025_cvpr_clls.md)
- [TOTP — ICCV 2025](papers/2025_iccv_totp.md)

### Object-centric / world dynamics
- [SlotFormer — ICLR 2023](papers/2023_iclr_slotformer.md)
- [DriveWorld — CVPR 2024](papers/2024_cvpr_driveworld.md)
- [LPWM — ICLR 2026](papers/2026_iclr_lpwm.md)

### Modern MOT motion reasoning
- [HyperSSM — CVPR 2026](papers/2026_cvpr_hyperssm.md)

## Priority

**Must address directly:** SURGE, StreamMOTP, PF-Track, TOTP, HyperSSM, LPWM, LG-ODE.  
**Prevents weak novelty claims:** PnPNet, PermaTrack, DreamTrack, SlotFormer, DriveWorld, IMSETrack.  
**Design/evaluation lessons:** FLN, CLLS, object-permanence papers, Loci.

## Working novelty boundary

> The ingredients are individually established. The current open question is whether online MOT benefits from inference over a **persistent object-specific stochastic latent-flow belief**, where learned multimodal MTP is the predictive transition mechanism, ambiguous observations are associated to identities using that predictive belief, and later observations explicitly revise the same future belief.

This remains a **working research gap**, not a publication claim.

See [NOVELTY_MATRIX.md](NOVELTY_MATRIX.md).
