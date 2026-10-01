# Learning To Track With Object Permanence

- **Venue:** ICCV 2021
- **Family:** multi-object tracking / recurrent object permanence
- **Canonical source:** https://openaccess.thecvf.com/content/ICCV2021/html/Tokmakov_Learning_To_Track_With_Object_Permanence_ICCV_2021_paper.html
- **MOTPT collision risk:** **High**

## Problem

The work asks how tracking can remain robust when instantaneous observations fail, especially during complete occlusion.

## Method

It extends CenterTrack to arbitrary-length video with recurrent spatio-temporal memory and studies supervision for invisible objects using synthetic data with behind-occlusion labels.

## Why it is close to MOTPT

It is strong prior art for long-lived state, full-history recurrent tracking and persistence through missing observations.

## Critical difference

Its central target is object permanence/localization and robust tracking; it does not make a persistent multimodal future posterior that is repeatedly corrected by observations the main state.

## Reusable lesson / pitfall

Invisible-object supervision can force synthetic annotations. MOTPT should first avoid making a correct invisible bbox at every frame the required target; belief persistence and bbox emission should be separable.

## MOTPT takeaway

This note is a **literature interpretation**, not accepted MOTPT evidence. Revise it if deeper reading changes the comparison, and cite the original paper rather than this note.
