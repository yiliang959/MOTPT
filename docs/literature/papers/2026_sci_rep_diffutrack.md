# DiffuTrack — Robust Online MOT with Conditional Diffusion Motion Hypotheses

- **Venue:** Scientific Reports 2026
- **Family:** probabilistic motion prediction / conditional diffusion / online MOT association
- **Canonical source:** https://doi.org/10.1038/s41598-026-50731-8
- **MOTPT collision risk:** **Critical / Very High**

## Problem

DiffuTrack targets two failure modes of online tracking-by-detection: deterministic unimodal motion propagation under nonlinear motion/ambiguity, and stale appearance representations after long gaps.

## Method

Its Motion Diffusion Module conditions on a fixed-length track-history window and generates a distribution of plausible bounding-box motion hypotheses with diffusion/DDIM sampling. These hypotheses are used directly in standard online predict-associate-update tracking. A separate time-aware prototype module handles appearance aging.

## Why it is close to MOTPT

This paper already establishes all of the following inside real online MOT:

- motion should be distributional rather than one deterministic point;
- multiple plausible futures help preserve candidate support under nonlinear motion;
- probabilistic future hypotheses can directly improve association;
- uncertainty/coverage can be analyzed rather than reporting only point prediction error.

Therefore MOTPT **cannot** claim “multimodal MTP feedback improves MOT association” as its core novelty.

## Critical difference

DiffuTrack conditions each prediction on a **fixed-length recent history** and uses the generated distribution as a motion prior for the current association step. The central research object is probabilistic motion propagation.

MOTPT must establish a stronger longitudinal object:

1. a persistent belief that survives the full tracked lifetime rather than being re-created from a fixed recent window;
2. explicit observation assimilation into that belief;
3. evaluation of how belief about the **same future target/event** changes as observations accumulate;
4. coupling of persistent identity belief and future belief, not only motion gating.

If MOTPT reduces to “replace deterministic motion with a stronger multimodal predictor,” DiffuTrack substantially weakens the contribution.

## Reusable lesson / pitfall

- Distributional coverage should be measured, not only minADE/minFDE.
- A fixed-window conditional diffusion predictor is an essential control/nearest-neighbor baseline conceptually.
- Association-centric diagnostics should attribute gains to nonlinear/occlusion cases.
- Sampling cost matters; the first MOTPT prototype should not assume an expensive diffusion model is necessary.

## MOTPT takeaway

The defensible gap is now **persistent observation-updated belief refinement**, not probabilistic motion hypotheses by themselves.
