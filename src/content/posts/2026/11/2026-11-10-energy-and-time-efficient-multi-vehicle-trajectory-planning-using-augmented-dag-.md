---
title: "Energy- and Time-Efficient Multi-Vehicle Trajectory Planning Using Augmented DAG Search in Configuration Space"
date: 2026-11-10T16:34:29+00:00
source: "arXiv"
source_url: "https://arxiv.org/abs/2611.14299v1"
ext_id: "arxiv:2611.14299v1"
tags: ["hardware", "models", "security"]
summary: "Multi-vehicle trajectory planning for CAV requires balancing energy consumption and travel time while ensuring safety and scalability. While travel-time-optimal methods based on Integer Programming exhibit poor scalability in large-scale multi-vehicle scenarios, existing energy-oriented approaches fail to balance energy consumption and travel time. We extend a configuration-space framework for mul"
---

Multi-vehicle trajectory planning for CAV requires balancing energy consumption and travel time while ensuring safety and scalability. While travel-time-optimal methods based on Integer Programming exhibit poor scalability in large-scale multi-vehicle scenarios, existing energy-oriented approaches fail to balance energy consumption and travel time. We extend a configuration-space framework for multi-vehicle trajectory planning to jointly locally optimize travel time and energy consumption. A weighted energy-travel time objective is combined with an efficient augmented DAG search on two-dimensional decompositions of a high-dimensional configuration space, enabling scalable and collision-free coordination of large numbers of vehicles. Although the proposed framework is applicable to other traffic scenarios, such as roundabouts and vehicle-following, we focus on intersections as a representative and challenging planning problem. To further improve performance for our methodology, we also extend the method with an insertion-ordering heuristic that exploits reduced-space geometric information. Combined with nonlinear model predictive control, the proposed framework is shown to scale to 40 vehicles, outperform MILP-based and convex optimization baselines in dense intersections, and reduce energy consumption at equalized travel times relative to time-optimal planning.

[Read the original at arXiv →](https://arxiv.org/abs/2611.14299v1)
