# Object Permanence Emerges in a Random Walk along Memory

- **Venue:** ICML 2022
- **Family:** self-supervised memory / object permanence
- **Canonical source:** https://proceedings.mlr.press/v162/tokmakov22a.html
- **MOTPT collision risk:** **Medium–High**

## Problem

The paper asks how object permanence can be learned without direct invisible-location supervision or a prescribed object dynamics model.

## Method

A self-supervised temporal-coherence objective fits a random walk over a space-time memory graph; the resulting representation stores occluded objects and predicts their motion.

## Why it is close to MOTPT

It shows that persistent motion-aware hidden object representation can emerge from temporal objectives, so that alone is not novel.

## Critical difference

The work is not centered on a stochastic multimodal future posterior jointly controlling MOT association and being explicitly revised as observations arrive.

## Reusable lesson / pitfall

Not every latent-state property must receive direct labels. Predictive consistency and re-observation agreement may be useful supervision; however, permanence alone is insufficient as the MOTPT story.

## MOTPT takeaway

This note is a **literature interpretation**, not accepted MOTPT evidence. Revise it if deeper reading changes the comparison, and cite the original paper rather than this note.
