# DriveWorld — 4D Pre-trained Scene Understanding via World Models for Autonomous Driving

- **Venue:** CVPR 2024
- **Family:** world model / temporal latent dynamics / multi-task driving
- **Canonical source:** https://openaccess.thecvf.com/content/CVPR2024/html/Min_DriveWorld_4D_Pre-trained_Scene_Understanding_via_World_Models_for_Autonomous_CVPR_2024_paper.html
- **MOTPT collision risk:** **High**

## Problem

DriveWorld studies spatio-temporal representation learning from multi-camera driving video as a 4D scene-understanding problem.

## Method

Its Memory State-Space Model uses a Dynamic Memory Bank for temporal-aware latent dynamics and shared representations that support MOT, motion forecasting and other downstream tasks.

## Why it is close to MOTPT

It shows learned latent dynamics can benefit both MOT and forecasting, so shared temporal representation is not a sufficient contribution.

## Critical difference

DriveWorld is a broad scene/world-model pretraining framework. MOTPT is intended to be object-specific and to tie posterior dynamics directly to identity association and observation correction.

## Reusable lesson / pitfall

Do not expand MOTPT into a generic world model before validating the core tracking hypothesis. Also define coordinate frame / ego-motion assumptions early.

## MOTPT takeaway

This note is a **literature interpretation**, not accepted MOTPT evidence. Revise it if deeper reading changes the comparison, and cite the original paper rather than this note.
