---
title: "How suboptimal is my stochastic network controller allowed to be? Completion certificates with application to power grids hosting AI data centers"
date: 2026-10-02T13:17:30+00:00
source: "arXiv"
source_url: "https://arxiv.org/abs/2610.03275v1"
ext_id: "arxiv:2610.03275v1"
tags: ["hardware"]
summary: "Power grids are beginning to host AI data centers whose demand can change abruptly and in a correlated way, and operators and planners must decide whether existing controllers can absorb the resulting transients and where new flexibility is worth installing. We cast this as a question in stochastic control: how far from optimal is an implementable controller? For controlled diffusions with affine,"
---

Power grids are beginning to host AI data centers whose demand can change abruptly and in a correlated way, and operators and planners must decide whether existing controllers can absorb the resulting transients and where new flexibility is worth installing. We cast this as a question in stochastic control: how far from optimal is an implementable controller? For controlled diffusions with affine, state-independent actuation, additive and possibly degenerate noise and quadratic control cost, any Hamilton-Jacobi-Bellman (HJB) subsolution bounds the optimal cost from below and simulation bounds the deployed cost from above, so their gap certifies the permissible suboptimality. We construct subsolutions from path-integral control by completing the control geometry: enlarging the control Gramian until it matches the physical noise makes the problem linearly solvable, and its Feynman-Kac value is an automatic lower bound whose HJB residual is exactly the energy of the fictitious control. A dual noise-deflation construction can be tighter but requires a curvature condition. The geometry yields planning rules: price control authority in proportion to local noise variance, and use shadow values to guide sparse reinforcement. For nonlinear stochastic swing dynamics of the IEEE 118-bus system after a severe load loss, a simple generator controller is certified within 2.8% of optimal under homogeneous forcing; under heterogeneous forcing the gap is 39% with uniform prices and 1.2% once the same total authority is repriced, before any hardware is added.

[Read the original at arXiv →](https://arxiv.org/abs/2610.03275v1)
