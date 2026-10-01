# PF-Track — Standing Between Past and Future: Spatio-Temporal Modeling for Multi-Camera 3D MOT

- **Venue:** CVPR 2023
- **Family:** future reasoning for multi-object tracking
- **Canonical source:** https://openaccess.thecvf.com/content/CVPR2023/html/Pang_Standing_Between_Past_and_Future_Spatio-Temporal_Modeling_for_Multi-Camera_3D_CVPR_2023_paper.html
- **MOTPT collision risk:** **Very High**

## Problem

PF-Track targets 3D MOT and argues that both past history and future motion should be modeled for temporal continuity.

## Method

Tracked instances are object queries. Past Reasoning refines tracks from history; Future Reasoning predicts future trajectories that help maintain positions and re-associate after long occlusions.

## Why it is close to MOTPT

It already establishes future prediction → better tracking/re-association, which is one of the closest parts of the MOTPT story.

## Critical difference

MOTPT needs the predictive object belief itself to be persistent, multimodal and explicitly corrected by later observations. “Use future trajectories for re-association” is not enough novelty.

## Reusable lesson / pitfall

Treat PF-Track as a mandatory nearest-neighbor baseline/conceptual comparison. Evaluate identity switches and occlusion/re-association, not only aggregate accuracy.

## MOTPT takeaway

This note is a **literature interpretation**, not accepted MOTPT evidence. Revise it if deeper reading changes the comparison, and cite the original paper rather than this note.
