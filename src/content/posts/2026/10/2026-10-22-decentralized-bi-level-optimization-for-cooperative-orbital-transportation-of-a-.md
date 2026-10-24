---
title: "Decentralized Bi-Level Optimization for Cooperative Orbital Transportation of a Rigid Payload"
date: 2026-10-22T17:05:17+00:00
source: "arXiv"
source_url: "https://arxiv.org/abs/2610.31562v1"
ext_id: "arxiv:2610.31562v1"
tags: ["hardware"]
summary: "The rapid growth of the space economy, alongside increasing orbital congestion and debris, is driving demand for reliable on-orbit transportation of large and non-cooperative objects. Performing such transportation with a swarm of small spacecraft distributes risk and removes the single point of failure inherent to monolithic architectures, but requires solving a non-convex trajectory optimization"
---

The rapid growth of the space economy, alongside increasing orbital congestion and debris, is driving demand for reliable on-orbit transportation of large and non-cooperative objects. Performing such transportation with a swarm of small spacecraft distributes risk and removes the single point of failure inherent to monolithic architectures, but requires solving a non-convex trajectory optimization coupling every agent's cone-constrained thrust to the payload's rotational dynamics. Existing approaches span decentralized control laws with asymptotic guarantees but limited constraint enforcement, and centralized and partially centralized planners that reintroduce a single point of failure. In this work, we present a decentralized bi-level framework driven by exact gradients: the problem is split into an inner convex thrust allocation and an outer search over payload torque trajectories. This decomposition yields fuel-efficient solutions quickly, without requiring full NLP convergence, and at short timescales its performance scales with the number of agents. Theoretical convergence guarantees are established, and the method is validated through extensive Monte Carlo simulation, including closed-loop recovery from in-flight faults. These properties make the framework well suited to spacecraft swarm applications.

[Read the original at arXiv →](https://arxiv.org/abs/2610.31562v1)
