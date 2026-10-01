# Loci — Learning What and Where: Disentangling Location and Identity Tracking Without Supervision

- **Venue:** ICLR 2023
- **Family:** object-centric representation / identity-location disentanglement
- **Canonical source:** https://openreview.net/pdf?id=NeDc-Ak-H_
- **MOTPT collision risk:** **High**

## Problem

Loci studies self-supervised decomposition of video into persistent entities while separately representing what an object is and where it is.

## Method

It uses slot-wise disentangled identity/content and location encodings; predictive-coding-like updates promote stable binding, while interactions and dynamics are modeled in latent space.

## Why it is close to MOTPT

The overlap includes persistent object state, identity/location separation, latent dynamics and recurrent incorporation of visual evidence.

## Critical difference

Loci is an object-centric scene reasoning framework rather than standard detection-based online MOT with uncertain association plus an explicit MTP posterior used as transition/likelihood.

## Reusable lesson / pitfall

Identity evidence and dynamical state may benefit from factorization. But using what/where tokens is not enough; MOTPT needs future-belief and association semantics.

## MOTPT takeaway

This note is a **literature interpretation**, not accepted MOTPT evidence. Revise it if deeper reading changes the comparison, and cite the original paper rather than this note.
