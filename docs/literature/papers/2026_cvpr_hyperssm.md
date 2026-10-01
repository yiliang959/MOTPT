# HyperSSM — Hypergraph-State Collaborative Reasoning for Multi-Object Tracking

- **Venue:** CVPR 2026
- **Family:** MOT / state-space motion reasoning / multi-object interaction
- **Canonical source:** https://openaccess.thecvf.com/content/CVPR2026/html/Song_Hypergraph-State_Collaborative_Reasoning_for_Multi-Object_Tracking_CVPR_2026_paper.html
- **MOTPT collision risk:** **Very High**

## Problem

HyperSSM targets noisy motion prediction and trajectory fragmentation under occlusion in MOT, including the idea that correlated targets should constrain each other.

## Method

A Hypergraph captures high-order inter-object motion correlations, while a State Space Model provides structured temporal transitions. It evaluates on MOT17, MOT20, DanceTrack and SportsMOT.

## Why it is close to MOTPT

It strongly blocks the claim that modern MOT lacks learned persistent dynamical state or state-space motion reasoning.

## Critical difference

HyperSSM focuses on motion estimation/stability. MOTPT proposes a stochastic multimodal future belief with prediction/observation correction semantics and explicit future-refinement evaluation.

## Reusable lesson / pitfall

Use a state-space hidden-state baseline of similar capacity. MOTPT diagnostics must prove more than “better temporal motion features.”

## MOTPT takeaway

This note is a **literature interpretation**, not accepted MOTPT evidence. Revise it if deeper reading changes the comparison, and cite the original paper rather than this note.
