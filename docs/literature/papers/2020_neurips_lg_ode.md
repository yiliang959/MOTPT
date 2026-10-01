# LG-ODE — Learning Continuous System Dynamics from Irregularly-Sampled Partial Observations

- **Venue:** NeurIPS 2020
- **Family:** partial-observation latent dynamics / continuous-time dynamics
- **Canonical source:** https://proceedings.neurips.cc/paper/2020/hash/ba4849411c8bbdd386150e5e32204198-Abstract.html
- **MOTPT collision risk:** **High**

## Problem

LG-ODE studies multi-agent dynamical systems when observations are irregularly sampled and only part of the system is observed. The structural objects/graph are defined, while continuous latent dynamics must be inferred from partial trajectories.

## Method

It encodes irregular partial observations with a graph neural network, infers latent initial states, and evolves them with a latent Neural ODE.

## Why it is close to MOTPT

The conceptual overlap is strong: discrete/partial observations constrain a persistent latent dynamical process, and that process supports future inference.

## Critical difference

LG-ODE does not solve the central online MOT correspondence problem: it does not need to decide which ambiguous current visual detection belongs to which persistent physical identity. MOTPT therefore cannot claim “partial observations → latent dynamics” as new; it must couple learned dynamics with uncertain identity/association.

## Reusable lesson / pitfall

Make the observation-time versus latent-dynamics distinction explicit. A latent-flow claim also needs controls against simple coordinate-history encoders and generic recurrent states.

## MOTPT takeaway

This note is a **literature interpretation**, not accepted MOTPT evidence. Revise it if deeper reading changes the comparison, and cite the original paper rather than this note.
