---
title: "Hierarchical Agglomerative Clustering for Efficient Annual Voltage Security Assessment in Very-High RES Penetrated Power Systems"
date: 2026-08-28T12:59:15+00:00
source: "arXiv"
source_url: "https://arxiv.org/abs/2608.28296v1"
tags: ["hardware"]
summary: "Voltage security assessment in power systems with high renewable energy source (RES) penetration requires analyzing many operating conditions to capture variability and uncertainty, but simulating a full year of operating points is computationally costly - motivating the selection of representative operating points (ROPs). Most existing methods cluster demand and generation profiles, but similarit"
---

Voltage security assessment in power systems with high renewable energy source (RES) penetration requires analyzing many operating conditions to capture variability and uncertainty, but simulating a full year of operating points is computationally costly - motivating the selection of representative operating points (ROPs). Most existing methods cluster demand and generation profiles, but similarity in these profiles does not guarantee similarity in voltage behavior, since reactive power limits, voltage-control actions, and nonlinear network interactions shape voltage response in ways that cannot be inferred from power profile patterns. This paper proposes an unsupervised learning framework that selects ROPs based on the system's actual voltage response: each operating point is represented by system-wide voltage-risk indices from AC power-flow solutions, Principal Component Analysis reduces dimensionality, and Hierarchical Agglomerative Clustering with Ward linkage identifies representative voltage regimes. A comprehensive set of evaluation criteria then measures how well the selected ROPs reproduce the full year's voltage-security characteristics under normal and contingency conditions. On the IEEE Voltage Test System under very high RES penetration, the framework reduces the annual operating point set by 99.66 percent while reproducing full-year voltage behavior with 98.3 percent reconstruction accuracy in steady state and 93.4 percent in post-contingency response, outperforming existing injection-space clustering and heuristic sampling.

[Read the original at arXiv →](https://arxiv.org/abs/2608.28296v1)
