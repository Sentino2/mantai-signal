---
title: "Efficient ADMM for Soft-Constrained Quadratic Programs via Generalized Slack Projections"
date: 2026-10-26T15:41:36+00:00
source: "arXiv"
source_url: "https://arxiv.org/abs/2610.35631v1"
ext_id: "arxiv:2610.35631v1"
tags: ["hardware"]
summary: "Quadratic programs (QPs) are a core building block in many applications. In practice, constraints are often softened with slack variables to guarantee feasibility. The standard approach tackles this by introducing additional decision variables, growing the resulting optimization problem. In this paper, we propose an Alternating Direction Method of Multipliers (ADMM) scheme for a broad class of con"
---

Quadratic programs (QPs) are a core building block in many applications. In practice, constraints are often softened with slack variables to guarantee feasibility. The standard approach tackles this by introducing additional decision variables, growing the resulting optimization problem. In this paper, we propose an Alternating Direction Method of Multipliers (ADMM) scheme for a broad class of convex slack penalty functions, including all $\ell_k$-norms, without increasing the problem size. The only change to the ADMM scheme is a modified slack projection function, while the remaining algorithm stays the same. We demonstrate our approach on numerical examples, showing significant speedups, and show its flexibility on an energy optimization problem.

[Read the original at arXiv →](https://arxiv.org/abs/2610.35631v1)
