# SURGE — Approximation and Training Free Particle Filter for Diffusion Surrogate

- **Venue:** ICML 2026
- **Family:** data assimilation / diffusion forecasting / particle filtering
- **Canonical source:** https://proceedings.mlr.press/v306/wei26w.html
- **MOTPT collision risk:** **Very High at the inference-principle level**

## Problem

SURGE studies sequential latent-state estimation from noisy partial observations when a pretrained diffusion model acts as a dynamical surrogate forecaster.

## Method

It combines observation-likelihood guidance with Sequential Monte Carlo over diffusion trajectories, importance weighting and resampling to approximate the observation-conditioned posterior.

## Why it is close to MOTPT

It is extremely close to MOTPT's forecast → observe → correct semantics and explicitly studies continuous correction/progressive trajectory refinement.

## Critical difference

It is not MOT: ambiguous object identity/data association is not the central hidden variable. MOTPT must couple learned forecasting with competing detection-to-identity hypotheses rather than rediscover data assimilation.

## Reusable lesson / pitfall

Acknowledge Bayesian/data-assimilation ancestry explicitly. SURGE is also a strong design reference if MOTPT later uses sample/particle reweighting.

## MOTPT takeaway

This note is a **literature interpretation**, not accepted MOTPT evidence. Revise it if deeper reading changes the comparison, and cite the original paper rather than this note.
