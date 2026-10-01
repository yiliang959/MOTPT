# StreamMOTP — Streaming and Unified Framework for Joint 3D Multi-Object Tracking and Trajectory Prediction

- **Venue:** ACCV 2024
- **Family:** joint streaming tracking + trajectory prediction
- **Canonical source:** https://openaccess.thecvf.com/content/ACCV2024/html/Zhuang_StreamMOTP_Streaming_and_Unified_Framework_for_Joint_3D_Multi-Object_Tracking_ACCV_2024_paper.html
- **MOTPT collision risk:** **Very High**

## Problem

StreamMOTP directly addresses joint 3D MOT and trajectory prediction, including limitations of single-frame training and coordinate inconsistency between the two tasks.

## Method

It is streaming, maintains long-term latent track features in a memory bank, uses relative spatio-temporal positional encoding and a dual-stream future predictor.

## Why it is close to MOTPT

It is the clearest prior work against “MOT and MTP have not been integrated”: it already provides a streaming unified architecture with persistent memory.

## Critical difference

MOTPT must differ at the inference-semantics level: stochastic object belief, MTP as transition/likelihood mechanism, explicit observation correction and same-future belief refinement—not only shared memory and two tasks.

## Reusable lesson / pitfall

Coordinate representation mismatch is a known problem. Decide image, ego-compensated or world-relative flow instead of treating coordinates as a minor implementation detail.

## MOTPT takeaway

This note is a **literature interpretation**, not accepted MOTPT evidence. Revise it if deeper reading changes the comparison, and cite the original paper rather than this note.
