---
title: "Policy Synthesis for Finite Populations of MDP Agents under Aggregate Reach-Avoid Chance Constraints"
date: 2026-10-08T14:23:58+00:00
source: "arXiv"
source_url: "https://arxiv.org/abs/2610.12028v1"
ext_id: "arxiv:2610.12028v1"
tags: ["hardware", "traction"]
summary: "Consider a finite population of agents with decoupled Markov transition dynamics and empirical-density feedback, subject to the following constraints: with probability at least $1-δ_r$, at least a fraction $α_r$ of agents must reach a target region at some time $t^*$, while, at each time up to $t^*$, the unsafe population fraction must remain below $β_u$ with probability at least $1-δ_u$. However,"
---

Consider a finite population of agents with decoupled Markov transition dynamics and empirical-density feedback, subject to the following constraints: with probability at least $1-δ_r$, at least a fraction $α_r$ of agents must reach a target region at some time $t^*$, while, at each time up to $t^*$, the unsafe population fraction must remain below $β_u$ with probability at least $1-δ_u$. However, standard mean-field methods enforce these constraints only in expectation, which fails to account for stochastic fluctuations at finite fleet size $N$. To address this control problem, we propagate the second-order moment (variance) of the empirical density alongside the mean-field trajectory via a discrete-time Lyapunov recursion, and apply the Cantelli inequality to convert chance constraints into tractable deterministic conditions on the moments of the empirical density. We then incorporate these moment-based surrogate constraints into a gradient-based sequential convex approximation procedure for density-feedback policy synthesis. We further introduce additional moment-error bounds to construct a rigorous finite-$N$ certificate. The method is evaluated on a gridworld environment and a power-system EV-charging aggregation problem and compared with a standard deterministic population-level LP baseline.

[Read the original at arXiv →](https://arxiv.org/abs/2610.12028v1)
