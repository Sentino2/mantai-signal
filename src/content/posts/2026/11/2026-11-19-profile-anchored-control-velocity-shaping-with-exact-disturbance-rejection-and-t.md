---
title: "Profile-Anchored Control: Velocity Shaping with Exact Disturbance Rejection and Transient-Free Replanning"
date: 2026-11-19T17:21:02+00:00
source: "arXiv"
source_url: "https://arxiv.org/abs/2611.26454v1"
ext_id: "arxiv:2611.26454v1"
tags: ["hardware"]
summary: "In many motion-control problems, how a target is approached matters as much as whether it is reached: speed and deceleration must stay within actuator, safety or comfort limits despite unknown loads and disturbances. Position-dependent velocity profiles provide a natural way to describe such requirements. We show that the square of such a profile can be used both to plan the motion and to construc"
---

In many motion-control problems, how a target is approached matters as much as whether it is reached: speed and deceleration must stay within actuator, safety or comfort limits despite unknown loads and disturbances. Position-dependent velocity profiles provide a natural way to describe such requirements. We show that the square of such a profile can be used both to plan the motion and to construct the controller that executes it. Our main result, profile-anchored control with exact rejection (PACER), recovers the nominal motion after a finite time under an unknown gain and load, and then allows the profile to be replaced mid-motion without a transient. It combines a static law for scalar second-order systems with a dynamic law for first-order ones, used for disturbance rejection. The static law guarantees uniform global asymptotic stability under an unknown input gain with a known lower bound, and finite-time stability under local homogeneity, while the first-order law gives analogous guarantees under disturbances of bounded rate and provides the exact rejection in PACER. Replanning of a profile under speed, acceleration and jerk limits can be formulated as a convex program. The approach is illustrated on a simulated elevator.

[Read the original at arXiv →](https://arxiv.org/abs/2611.26454v1)
