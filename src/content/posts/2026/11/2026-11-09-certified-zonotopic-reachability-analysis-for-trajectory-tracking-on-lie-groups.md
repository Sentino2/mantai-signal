---
title: "Certified Zonotopic Reachability Analysis for Trajectory Tracking on Lie Groups"
date: 2026-11-09T17:40:43+00:00
source: "arXiv"
source_url: "https://arxiv.org/abs/2611.12767v1"
ext_id: "arxiv:2611.12767v1"
tags: ["hardware"]
summary: "Autonomous vehicles track planned trajectories close to obstacles. Unknown disturbances make them deviate from these trajectories. With a bound on the tracking error that disturbances can cause, a planned trajectory can be certified as safe before execution. Existing set-based methods bound the tracking error by one invariant ellipsoid for the whole trajectory or by intervals, which are both conse"
---

Autonomous vehicles track planned trajectories close to obstacles. Unknown disturbances make them deviate from these trajectories. With a bound on the tracking error that disturbances can cause, a planned trajectory can be certified as safe before execution. Existing set-based methods bound the tracking error by one invariant ellipsoid for the whole trajectory or by intervals, which are both conservative. For aerial and space vehicles, the tracking error evolves on a matrix Lie group with nonlinear dynamics. However, for group-affine systems, the error dynamics are linear in Lie algebra coordinates when the vehicle receives the inputs of the reference. The control input and the disturbance enter through the inverse right Jacobian, a matrix that depends on the error. We propagate the linear part of the error dynamics with zonotopes and enclose the effect of the inverse right Jacobian on the disturbance in closed form. The resulting tubes are tight and provably contain all reachable tracking errors in continuous time. When some error components have no input, the inverse right Jacobian leaves unmatched nonlinear terms in the closed loop. None of the tested methods certifies such a closed loop. Hybrid coordinates make these terms matched, so that our controller cancels every nonlinear term that does not contain the disturbance. Our tubes give tighter bounds than the ellipsoid method in simulations of a planar aircraft and a fully actuated multirotor and in real flights of a quadrotor, where the tube contains every measured attitude error. Under larger disturbances and the same feedback gain, the ellipsoid method yields no valid ellipsoid, whereas our tubes remain valid.

[Read the original at arXiv →](https://arxiv.org/abs/2611.12767v1)
