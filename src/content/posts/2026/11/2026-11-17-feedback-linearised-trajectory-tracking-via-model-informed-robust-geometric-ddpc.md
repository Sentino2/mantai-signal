---
title: "Feedback-Linearised Trajectory Tracking via Model-Informed Robust Geometric DDPC"
date: 2026-11-17T18:56:09+00:00
source: "arXiv"
source_url: "https://arxiv.org/abs/2611.23215v1"
ext_id: "arxiv:2611.23215v1"
tags: ["hardware", "models"]
summary: "Data-driven predictive control (DDPC) predicts system responses from recorded trajectories, but nonlinear dynamics can limit the accuracy of fixed linear predictors. This paper studies geometric robust DDPC for trajectory tracking of a fully actuated manipulator using model-based feedback linearisation. A mechanical model maps virtual acceleration commands into joint torques, while recorded data c"
---

Data-driven predictive control (DDPC) predicts system responses from recorded trajectories, but nonlinear dynamics can limit the accuracy of fixed linear predictors. This paper studies geometric robust DDPC for trajectory tracking of a fully actuated manipulator using model-based feedback linearisation. A mechanical model maps virtual acceleration commands into joint torques, while recorded data capture residual dynamics arising from imperfect model parameters. The controller minimises worst-case prediction error over an open Grassmannian ball centred at the fitted trajectory subspace. Simulations on a planar 2R manipulator under gravity compare the proposed method with double-integrator model predictive control (MPC) and direct regularised data-enabled predictive control (DeePC). Results show improved tracking over double-integrator MPC despite increased torque effort, while performance relative to DeePC depends on the reference trajectory.

[Read the original at arXiv →](https://arxiv.org/abs/2611.23215v1)
