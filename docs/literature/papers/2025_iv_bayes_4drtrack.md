# Bayes-4DRTrack — Bayesian Approximation-Based Trajectory Prediction and Tracking with 4D Radar

- **Venue:** IEEE Intelligent Vehicles Symposium (IV) 2025
- **Family:** Bayesian uncertainty / learned nonlinear motion prediction / 3D MOT
- **Canonical source:** https://doi.org/10.1109/IV64158.2025.11097628
- **MOTPT collision risk:** **Very High for “Bayesian + learned prediction inside MOT”**

## Problem

The work targets 4D-radar 3D MOT under nonlinear motion and uncertainty, arguing that conventional Kalman filtering with fixed covariance is too rigid for abrupt maneuvers.

## Method

Bayes-4DRTrack combines a Transformer-based motion prediction network with Bayesian approximation in detection/prediction and a Doppler-aware two-stage association strategy.

## Why it is close to MOTPT

It already combines learned nonlinear trajectory/motion prediction, Bayesian uncertainty estimation and multi-object tracking. Therefore MOTPT cannot claim novelty from simply replacing a Kalman transition with a Transformer predictor or from adding Bayesian uncertainty to MOT.

## Critical difference

The reported formulation is centered on uncertainty-aware state prediction/association for radar MOT. MOTPT's stronger target is a **persistent multimodal future belief** whose alternative futures are longitudinally revised by subsequent observations and whose identity association is part of that same assimilation process.

## Reusable lesson / pitfall

A direct classical-filter versus learned-predictor comparison is necessary. MOTPT also needs evidence that multimodal posterior refinement provides something beyond uncertainty-scaled single-state prediction.

## MOTPT takeaway

Treat “Bayesian deep MOT + learned predictor” as established prior art. The differentiator must be identity-aware multimodal belief assimilation and same-future refinement, not the words Bayesian or prediction.
