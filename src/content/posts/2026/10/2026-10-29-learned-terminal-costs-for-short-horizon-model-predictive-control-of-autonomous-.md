---
title: "Learned Terminal Costs for Short-Horizon Model Predictive Control of Autonomous Trucks in Interactive Highway Traffic"
date: 2026-10-29T15:23:51+00:00
source: "arXiv"
source_url: "https://arxiv.org/abs/2610.40257v1"
ext_id: "arxiv:2610.40257v1"
tags: ["hardware", "models"]
summary: "Autonomous highway driving for heavy-duty trucks is a challenging control problem. The greater mass, dimensions and intricate dynamics increase the requirements for cooperation from surrounding traffic in critical maneuvers, requiring a careful balance between safety constraints and efficient long-horizon decision making. Model Predictive Control (MPC) provides rigorous constraint satisfaction but"
---

Autonomous highway driving for heavy-duty trucks is a challenging control problem. The greater mass, dimensions and intricate dynamics increase the requirements for cooperation from surrounding traffic in critical maneuvers, requiring a careful balance between safety constraints and efficient long-horizon decision making. Model Predictive Control (MPC) provides rigorous constraint satisfaction but relies on terminal cost which can limit its effectiveness at short, computationally affordable horizons. Reinforcement Learning (RL) captures long-term driving behavior but offers no constraint guarantees and tends toward overly conservative policies when trained under sparse collision penalties. In this paper, we propose a hybrid MPC and RL framework for highway driving in autonomous trucks, where a finite-horizon MPC, solved via dynamic programming, uses a pre-trained RL model for terminal cost estimation. We evaluate the framework in a simulation environment with reactive surrounding traffic and compare it against pure MPC with zero terminal cost, rollout with terminal cost estimation using a base policy, and pure RL. Results show that the hybrid approach achieves zero collisions with the lowest cost of any configuration.

[Read the original at arXiv →](https://arxiv.org/abs/2610.40257v1)
