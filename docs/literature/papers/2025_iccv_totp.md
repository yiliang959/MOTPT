# TOTP — Transferable Online Pedestrian Trajectory Prediction with Temporal-Adaptive Mamba Latent Diffusion

- **Venue:** ICCV 2025
- **Family:** online trajectory prediction / variable observations / latent diffusion
- **Canonical source:** https://openaccess.thecvf.com/content/ICCV2025/html/Ren_TOTP_Transferable_Online_Pedestrian_Trajectory_Prediction_with_Temporal-Adaptive_Mamba_Latent_ICCV_2025_paper.html
- **MOTPT collision risk:** **Very High**

## Problem

TOTP explicitly formulates online pedestrian trajectory prediction with variable observations instead of waiting for a fixed-length history.

## Method

It uses Mamba temporal modeling and latent diffusion to represent future motion trends and sample future trajectories under different observation constraints.

## Why it is close to MOTPT

It removes two easy claims: online MTP is not new, and variable-observation latent multimodal prediction is not new.

## Critical difference

The prediction target identity is already defined. TOTP does not solve ambiguous detection-to-track correspondence or use its predictive distribution as the persistent state for identity inference.

## Reusable lesson / pitfall

Use it as a prediction-side baseline/reference. MOTPT must add identity association and longitudinal same-future belief-refinement experiments.

## MOTPT takeaway

This note is a **literature interpretation**, not accepted MOTPT evidence. Revise it if deeper reading changes the comparison, and cite the original paper rather than this note.
