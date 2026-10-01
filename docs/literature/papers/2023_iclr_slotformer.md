# SlotFormer — Unsupervised Visual Dynamics Simulation with Object-Centric Models

- **Venue:** ICLR 2023
- **Family:** object-centric latent dynamics / world models
- **Canonical source:** https://slotformer.github.io/
- **MOTPT collision risk:** **High**

## Problem

SlotFormer asks how learned object-centric representations can support long-term visual dynamics simulation and downstream reasoning.

## Method

It applies an autoregressive Transformer over object slots, models spatio-temporal relationships and predicts future object states for video prediction, VQA and planning.

## Why it is close to MOTPT

It establishes strong prior art for object-specific latent dynamics, persistent object representations and future prediction in latent space.

## Critical difference

Standard MOT identity association under detector ambiguity is not the central inference problem, and observation-conditioned refinement of the same future belief is not the primary target.

## Reusable lesson / pitfall

MOTPT need not solve full video reconstruction or unsupervised slot discovery. Use existing object hypotheses to focus capacity on tracking-specific predictive belief.

## MOTPT takeaway

This note is a **literature interpretation**, not accepted MOTPT evidence. Revise it if deeper reading changes the comparison, and cite the original paper rather than this note.
