# Gated Temporal Fusion Transformers for Robust Multi-Object Tracking

- **Venue:** WACV 2026
- **Family:** temporal memory / Transformer MOT / MOTIP enhancement
- **Canonical source:** https://doi.org/10.1109/WACV61042.2026.00440
- **MOTPT collision risk:** **High as a baseline-control**

## Problem

The work argues that Transformer MOT still underuses temporal information in dynamic/crowded scenes.

## Method

It introduces tracklet memory, encoder-level historical integration and gated temporal feature fusion. The framework is applied to several Transformer trackers, including MOTIP.

## Why it is close to MOTPT

It directly demonstrates that **MOTIP has measurable headroom from better temporal modeling**. Reported MOTIP+GTF results include 73.9 HOTA / 66.7 AssA on DanceTrack and 76.4 HOTA / 67.3 AssA on SportsMOT, with the SportsMOT result improving the cited MOTIP baseline by 1.2 HOTA and 1.9 AssA.

## Critical difference

GTF improves temporal representation/memory but does not formulate persistent stochastic multimodal future belief or same-future observation-driven refinement.

This makes it an important control: if MOTPT only improves MOTIP because “more history helps,” GTF already provides a simpler explanation.

## Reusable lesson / pitfall

A capacity-matched temporal-memory baseline is mandatory. MOTPT should demonstrate gains concentrated in cases where predictive uncertainty and future modes matter, not merely where extra temporal context helps.

## MOTPT takeaway

The baseline is breakable, but generic temporal fusion already breaks it. MOTPT must show **why future-belief feedback is necessary beyond memory**.
