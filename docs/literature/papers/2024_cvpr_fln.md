# FLN — Adapting to Length Shift: FlexiLength Network for Trajectory Prediction

- **Venue:** CVPR 2024
- **Family:** variable-observation trajectory prediction
- **Canonical source:** https://openaccess.thecvf.com/content/CVPR2024/html/Xu_Adapting_to_Length_Shift_FlexiLength_Network_for_Trajectory_Prediction_CVPR_2024_paper.html
- **MOTPT collision risk:** **Medium**

## Problem

FLN identifies Observation Length Shift: predictors trained on one standardized history duration may fail when available history length changes.

## Method

It trains on diverse lengths and introduces calibration/adaptation mechanisms to learn more length-robust temporal representations.

## Why it is close to MOTPT

It means MOTPT cannot claim that trajectory prediction is intrinsically tied to one fixed observation length.

## Critical difference

FLN asks for robust prediction under different input lengths. MOTPT instead maintains one recursively updated object belief across its lifetime and studies how that belief changes with new evidence.

## Reusable lesson / pitfall

No-fixed-window should be a requirement, not the novelty claim. Avoid repeated fixed-window re-encoding unless justified.

## MOTPT takeaway

This note is a **literature interpretation**, not accepted MOTPT evidence. Revise it if deeper reading changes the comparison, and cite the original paper rather than this note.
