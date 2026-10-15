---
title: "VIGOR-MPC: Vision-Guided Objective Regulation MPC"
date: 2026-10-14T15:15:32+00:00
source: "arXiv"
source_url: "https://arxiv.org/abs/2610.20333v1"
ext_id: "arxiv:2610.20333v1"
tags: ["hardware"]
summary: "Controlling an agent in an environment solely perceived through onboard vision is challenging: perception yields noisy, variable-length, and partially occluded context, while onboard compute is shared between perception and control, limiting the planning horizon executable in real time. We propose VIGOR-MPC, a modular student-teacher framework, agnostic to the perception pipeline, which addresses "
---

Controlling an agent in an environment solely perceived through onboard vision is challenging: perception yields noisy, variable-length, and partially occluded context, while onboard compute is shared between perception and control, limiting the planning horizon executable in real time. We propose VIGOR-MPC, a modular student-teacher framework, agnostic to the perception pipeline, which addresses reference tracking across navigation tasks by distilling a privileged, field-of-view-aware long-horizon MPC into a computationally lightweight short-horizon MPC whose cost parameters are determined online from vision. The teacher operates in simulation with full state knowledge and a multi-trajectory formulation that guarantees the agent can stay within its field of view. The student observes only the noisy, occluded context produced by a perception module and learns, via a multi-level recurrent mapping, to infer cost parameters that aim to recover the teacher's behavior despite missing information. We evaluate VIGOR-MPC on vision-based autonomous racing in simulation and on hardware. Using only onboard perception of the track, VIGOR-MPC generalizes to tracks unseen during training and approaches the lap times of the privileged long-horizon teacher while reducing per-step computation by over 90%.

[Read the original at arXiv →](https://arxiv.org/abs/2610.20333v1)
