# LPWM — Latent Particle World Models: Self-supervised Object-centric Stochastic Dynamics Modeling

- **Venue:** ICLR 2026
- **Family:** object-centric stochastic world model
- **Canonical source:** https://proceedings.iclr.cc/paper_files/paper/2026/hash/cf7ba4b2d14e0f6a0e8247af77745094-Abstract-Conference.html
- **MOTPT collision risk:** **Very High**

## Problem

LPWM studies self-supervised object-centric stochastic dynamics from video and scales object-centric world modeling toward real-world multi-object data.

## Method

It discovers object-related keypoints/boxes/masks and models stochastic object dynamics with latent particles, supporting prediction and downstream decision-making.

## Why it is close to MOTPT

It establishes object-centric latent state, stochastic multi-object dynamics and particle-like alternative futures as current prior art.

## Critical difference

LPWM is a world model rather than a standard online MOT association method. MOTPT can assume detector/track hypotheses and focus on the coupling between stochastic dynamics and persistent identity.

## Reusable lesson / pitfall

Particles/samples are a credible belief representation, but particles alone are not novelty. If used, show observation-driven reweighting improves identity and calibration.

## MOTPT takeaway

This note is a **literature interpretation**, not accepted MOTPT evidence. Revise it if deeper reading changes the comparison, and cite the original paper rather than this note.
