# CLLS — Adapting to Observation Length of Trajectory Prediction via Contrastive Learning

- **Venue:** CVPR 2025
- **Family:** observation-length adaptation / trajectory representation
- **Canonical source:** https://openaccess.thecvf.com/content/CVPR2025/html/Qiu_Adapting_to_Observation_Length_of_Trajectory_Prediction_via_Contrastive_Learning_CVPR_2025_paper.html
- **MOTPT collision risk:** **Medium**

## Problem

CLLS revisits observation-length shift and argues that representation robustness, not only architecture complexity, is central to adaptation.

## Method

It uses contrastive learning to encourage length-invariant trajectory features and combines it with a lightweight recurrent predictor.

## Why it is close to MOTPT

It further blocks variable observation length or recurrent history representation as standalone novelty.

## Critical difference

Length invariance is not a persistent posterior. MOTPT should preserve legitimate evidence-driven belief changes rather than mapping all history lengths to the same representation.

## Reusable lesson / pitfall

Include simple RNN/SSM capacity-matched controls. A complex belief architecture should beat strong lightweight temporal representations for the intended reason.

## MOTPT takeaway

This note is a **literature interpretation**, not accepted MOTPT evidence. Revise it if deeper reading changes the comparison, and cite the original paper rather than this note.
