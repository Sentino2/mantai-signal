---
title: "LACART: Lookahead-Augmented Collision Avoidance and Reference Tracking Strategies for Safety-Critical Robots"
date: 2026-11-06T15:52:50+00:00
source: "arXiv"
source_url: "https://arxiv.org/abs/2611.09640v1"
ext_id: "arxiv:2611.09640v1"
tags: ["hardware"]
summary: "Autonomous racing provides a demanding testbed for collision avoidance under tight geometric and computational constraints. Building on a recent conference contribution and a master's dissertation, LACART combines lookahead-based control barrier functions (CBFs), a relaxed control Lyapunov function (CLF), and quadratic programming (QP) to modify nominal vehicle commands for obstacle avoidance and "
---

Autonomous racing provides a demanding testbed for collision avoidance under tight geometric and computational constraints. Building on a recent conference contribution and a master's dissertation, LACART combines lookahead-based control barrier functions (CBFs), a relaxed control Lyapunov function (CLF), and quadratic programming (QP) to modify nominal vehicle commands for obstacle avoidance and reference tracking. The method handles circular obstacles and track boundaries in a common optimisation layer. Comparative simulation results against Huang \emph{et al.} \cite{r9} show similar full-track paths and lower median computation times: 0.31 versus 0.33 ms per step and 0.023 versus 0.025 ms per QP solve. The dissertation further demonstrates a 1:43-scale vehicle with camera-based estimation and wireless actuation at a reported 25 Hz control rate. We identify the conditions linking lookahead-point clearance to body clearance, illustrate hardware limitations, and propose a recorded demonstration of safety intervention and recovery. The contribution targets ground-robot collision avoidance and real-time safety monitoring.

[Read the original at arXiv →](https://arxiv.org/abs/2611.09640v1)
