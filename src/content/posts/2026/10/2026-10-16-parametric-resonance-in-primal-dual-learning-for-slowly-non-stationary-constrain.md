---
title: "Parametric Resonance in Primal-Dual Learning for Slowly Non-Stationary Constrained MDPs"
date: 2026-10-16T17:19:08+00:00
source: "arXiv"
source_url: "https://arxiv.org/abs/2610.23788v1"
ext_id: "arxiv:2610.23788v1"
tags: ["hardware"]
summary: "Primal-dual methods for constrained Markov decision processes are analyzed under a two-timescale assumption, with non-stationarity entering through two channels. In the additive channel, where the constraint level oscillates, the dual oscillation saturates at a floor set by the moving optimum and is amplified linearly by the timescale ratio. In the parametric channel, where the constraint sensitiv"
---

Primal-dual methods for constrained Markov decision processes are analyzed under a two-timescale assumption, with non-stationarity entering through two channels. In the additive channel, where the constraint level oscillates, the dual oscillation saturates at a floor set by the moving optimum and is amplified linearly by the timescale ratio. In the parametric channel, where the constraint sensitivity oscillates, a coherent modulation carries no resonant forcing at any depth: the dual update's stiffness modulation cancels the primal update's damping modulation. Instability instead comes from a mismatch between the constraint estimate used by the primal update and the measurement used by the dual update, producing a parametric resonance at twice the pair's natural frequency. The tolerated mismatch grows with the square root of the forcing bandwidth and collapses with the square root of the dual-to-primal step-size ratio. These results hold on the tangent linear-quadratic reduction around an active saddle, for one constraint and for $K$ constraints under a common modulation and an isotropy condition. Driving both updates from the same estimate removes the resonant forcing but introduces a stationary offset equal to the estimator's bias. In a Lagrangian soft actor-critic agent, the multiplier locks onto the sub-harmonic at the timescale ratios its identified linear loop predicts and a coherent cost critic suppresses the lock-in, while a proportional (PID) term, predicted to leave the lock-in in place, suppresses most of it through the projection of the multiplier.

[Read the original at arXiv →](https://arxiv.org/abs/2610.23788v1)
