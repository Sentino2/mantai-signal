---
title: "Parameter Estimation of Power Electronic Converters with Differentiable Physics Simulation"
date: 2026-08-31T14:57:50+00:00
source: "arXiv"
source_url: "https://arxiv.org/abs/2608.30915v1"
tags: ["hardware"]
summary: "This article proposes a differentiable physics simulation (DP simulation)-based parameter estimation method for the condition monitoring of power electronic converters. In the proposed method, the time-domain simulation of converter dynamics is embedded into a differentiable computational graph, directly linking device parameters to observed voltage and current trajectories. By formulating differe"
---

This article proposes a differentiable physics simulation (DP simulation)-based parameter estimation method for the condition monitoring of power electronic converters. In the proposed method, the time-domain simulation of converter dynamics is embedded into a differentiable computational graph, directly linking device parameters to observed voltage and current trajectories. By formulating differentiable time-stepping operators, the nonlinear dynamics of the converter across different circuit topologies are simulated in a unified, differentiable manner. A dc-dc buck converter is used as a representative case study. Using sparse transient samples from existing sensing channels, the method enables noninvasive parameter estimation without additional sensing hardware. Comprehensive simulation studies are conducted to evaluate the impacts of time-stepping schemes, regularization constraints, and various uncertainty sources on estimation accuracy and robustness. Subsequently, 30 distinct hardware configurations are experimentally tested for validation. The results show that the proposed method can effectively track the relative variations of health-related parameters across the critical components. This DP simulation framework provides a novel perspective for physics-informed machine learning in power electronic applications.

[Read the original at arXiv →](https://arxiv.org/abs/2608.30915v1)
