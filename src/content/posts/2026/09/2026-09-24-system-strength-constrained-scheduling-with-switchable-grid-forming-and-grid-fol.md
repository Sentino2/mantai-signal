---
title: "System Strength-Constrained Scheduling with Switchable Grid-Forming and Grid-Following Generation Resources"
date: 2026-09-24T11:34:23+00:00
source: "arXiv"
source_url: "https://arxiv.org/abs/2609.29412v1"
ext_id: "arxiv:2609.29412v1"
tags: ["hardware", "industrial", "traction"]
summary: "Inverter-based resources (IBRs) are increasingly dominating modern power systems, posing significant challenges to cost-effectively maintain system strength for stability. At the same time, the operating behaviors of IBRs are software-defined, including both their steady-state power outputs and control modes, e.g. grid-forming (GFM) and grid-following (GFL). Such flexibility has not been fully exp"
---

Inverter-based resources (IBRs) are increasingly dominating modern power systems, posing significant challenges to cost-effectively maintain system strength for stability. At the same time, the operating behaviors of IBRs are software-defined, including both their steady-state power outputs and control modes, e.g. grid-forming (GFM) and grid-following (GFL). Such flexibility has not been fully explored to efficiently operate future power systems. This paper develops a novel framework that simultaneously optimizes IBR operating behaviors and ensures adequate system strength. A comprehensive solution is provided to integrate system strength constraints into scheduling models, despite their inherent strong non-convexities. We derive a rigorous linear-matrix-inequality (LMI) reformulation of the system strength constraint, effectively addressing non-explicit formulations and dimension variation issues caused by GFM/GFL mode switching of IBRs. Then, we equivalently convert the original non-convex implicit system strength-constrained scheduling problem into an explicit mixed-integer semi-definite programming (MISDP) problem by incorporating the reformulated system strength constraint along with other operational constraints. We further provide a Rayleigh Cut method, which is compatible with standard mixed-integer linear programming (MILP) solvers, to solve this system strength-constrained scheduling problem. Case studies on a modified IEEE 118-bus system and a practical Jiangsu power system demonstrate the performance of the proposed methods.

[Read the original at arXiv →](https://arxiv.org/abs/2609.29412v1)
