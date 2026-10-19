---
title: "SparseMax-dSTL: Sound Robustness with Horizon-Independent Gradient Allocation for Temporal Logic Trajectory Optimization"
date: 2026-10-16T17:54:38+00:00
source: "arXiv"
source_url: "https://arxiv.org/abs/2610.23837v1"
ext_id: "arxiv:2610.23837v1"
tags: ["hardware"]
summary: "A gradient-based solver that enforces a Signal Temporal Logic (STL) specification uses a smooth approximation of its quantitative semantics, the robustness. In safety-critical trajectory optimization, this approximation must have two properties. First, it must be sound, that is, nonnegative only on trajectories that satisfy the specification. Second, at each temporal operator, the weight of its gr"
---

A gradient-based solver that enforces a Signal Temporal Logic (STL) specification uses a smooth approximation of its quantitative semantics, the robustness. In safety-critical trajectory optimization, this approximation must have two properties. First, it must be sound, that is, nonnegative only on trajectories that satisfy the specification. Second, at each temporal operator, the weight of its gradient on the violating samples must stay bounded away from zero, however long the horizon. The approximations in use, including the log-sum-exp, its sound variant, and the generalized-mean robustness, do not have both. We introduce lower approximations of the minimum and the maximum whose gradients are sparsemax projections, and we prove that the robustness built from them has both. It lies below the exact robustness and is therefore sound, and its error has a bound that is independent of the number of samples and known before optimization. The gradient of each approximation is exactly zero on every sample beyond a data-dependent threshold, so the weight on violating samples a gap beyond the others has a positive lower bound at every horizon. On a planar unicycle and on a seven-joint manipulator beside a person in simulation, the log-sum-exp approximation is positive on a violating trajectory. As the horizon of the manipulator's task grows from 10 to 80 s, the gradient weight of the sound variant on the violating samples falls from 0.22 to 0.04, while that of sparsemax stays at 1. In a constrained trajectory optimization of the unicycle, the constraint on the log-sum-exp robustness returns a violating trajectory, whereas the constraint on the sparsemax robustness returns a trajectory that satisfies the specification with the required margin.

[Read the original at arXiv →](https://arxiv.org/abs/2610.23837v1)
