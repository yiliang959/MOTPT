# PnPNet — End-to-End Perception and Prediction With Tracking in the Loop

- **Venue:** CVPR 2020
- **Family:** joint perception / tracking / motion forecasting
- **Canonical source:** https://openaccess.thecvf.com/content_CVPR_2020/html/Liang_PnPNet_End-to-End_Perception_and_Prediction_With_Tracking_in_the_Loop_CVPR_2020_paper.html
- **MOTPT collision risk:** **High**

## Problem

PnPNet jointly performs perception, online tracking and future motion forecasting for autonomous driving and argues that tracking should be inside the perception/prediction loop.

## Method

Tracks are updated online through association and trajectory estimation; trajectory-level track features are then used for forecasting in an end-to-end trainable model.

## Why it is close to MOTPT

It invalidates a weak claim that MOT/tracking and future forecasting have never been combined, and shows track history can be a forecasting substrate.

## Critical difference

MOTPT must go beyond Track → Forecast Head. Its predictive distribution should be part of the persistent state and should feed back into association/correction.

## Reusable lesson / pitfall

If prediction never changes the identity decision or the persistent belief, the distinction from this family becomes weak.

## MOTPT takeaway

This note is a **literature interpretation**, not accepted MOTPT evidence. Revise it if deeper reading changes the comparison, and cite the original paper rather than this note.
