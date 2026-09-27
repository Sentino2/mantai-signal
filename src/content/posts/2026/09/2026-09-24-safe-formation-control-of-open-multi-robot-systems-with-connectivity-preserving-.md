---
title: "Safe Formation Control of Open Multi-Robot Systems with Connectivity-Preserving Reconfiguration"
date: 2026-09-24T15:03:53+00:00
source: "arXiv"
source_url: "https://arxiv.org/abs/2609.29939v1"
ext_id: "arxiv:2609.29939v1"
tags: ["hardware"]
summary: "We address the formation control problem for open multi-robot systems (OMRS), i.e., systems in which robots may join or leave the team during operation and new interaction links are established over time, subject to inter-robot collision-avoidance and connectivity-maintenance constraints. The robots are modeled by double integrators, and interact over a dynamic undirected graph. We design a distri"
---

We address the formation control problem for open multi-robot systems (OMRS), i.e., systems in which robots may join or leave the team during operation and new interaction links are established over time, subject to inter-robot collision-avoidance and connectivity-maintenance constraints. The robots are modeled by double integrators, and interact over a dynamic undirected graph. We design a distributed controller based on the gradient of a barrier-Lyapunov function. To enable team reconfiguration, we introduce a formation manager that coordinates robot additions and removals and establishes prospective edges whenever needed, either to connect a joining robot to the team or to preserve connectivity before a robot departs. The upper-distance constraints of prospective edges are temporarily relaxed through auxiliary dynamics that preserve feasibility while progressively recovering the nominal interaction range. The resulting open-team dynamics are modeled as a switched system, for which we establish uniform practical stability for almost all initial conditions under a transition-dependent average dwell-time condition. Finally, the proposed approach is validated in realistic Gazebo simulations with dynamically simulated quadrotors undergoing repeated joining and departure maneuvers.

[Read the original at arXiv →](https://arxiv.org/abs/2609.29939v1)
