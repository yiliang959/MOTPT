# Learning Object Permanence from Video

- **Venue:** ECCV 2020
- **Family:** object permanence / invisible-object reasoning
- **Canonical source:** https://research.nvidia.com/publication/2020-10_learning-object-permanence-video
- **MOTPT collision risk:** **Medium–High**

## Problem

The paper asks whether a model can reason about objects that remain physically present when not directly visible, separating visible, occluded, contained and carried cases.

## Method

OPNet learns object localization across these visibility regimes on labeled video derived from CATER.

## Why it is close to MOTPT

It directly supports the premise that no current observation does not imply that the underlying object state stops existing.

## Critical difference

The main target is invisible-object localization/reasoning, not multimodal future belief, repeated posterior refinement, or ambiguous multi-object association in modern MOT.

## Reusable lesson / pitfall

Keep internal belief, current observability and externally emitted bbox as separate variables. Persistent belief should not force hallucinated tracker output.

## MOTPT takeaway

This note is a **literature interpretation**, not accepted MOTPT evidence. Revise it if deeper reading changes the comparison, and cite the original paper rather than this note.
