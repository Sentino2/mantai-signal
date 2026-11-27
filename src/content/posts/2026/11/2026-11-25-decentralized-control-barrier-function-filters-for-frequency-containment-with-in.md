---
title: "Decentralized Control Barrier Function Filters for Frequency Containment With Inverters"
date: 2026-11-25T15:31:58+00:00
source: "arXiv"
source_url: "https://arxiv.org/abs/2611.34558v1"
ext_id: "arxiv:2611.34558v1"
tags: ["hardware", "industrial", "models", "traction"]
summary: "This paper addresses the design of safety filters for grid-following (GFL) inverters in power transmission systems. The goal of the filters is to constrain frequency nadir and zenith following generation-demand imbalances, by supplementing primary frequency control. Using a reduced electromechanical model and control barrier functions (CBFs), we define an ideal filter through a convex quadratic pr"
---

This paper addresses the design of safety filters for grid-following (GFL) inverters in power transmission systems. The goal of the filters is to constrain frequency nadir and zenith following generation-demand imbalances, by supplementing primary frequency control. Using a reduced electromechanical model and control barrier functions (CBFs), we define an ideal filter through a convex quadratic program (QP). The ideal QP filter renders the set of admissible frequencies forward invariant; however, its direct implementation is impractical, as it requires centralized implementation and model-based computation. We then use a dual proximal formulation and a two-time-scale implementation to obtain decentralized dynamic filters that can be implemented at each inverter and use only local frequency and rate-of-change-of-frequency estimates. To assess the performance and the ability to regulate frequency, we derive bounds on the distance between state trajectories under the dynamic and ideal CBF filters. The bounds quantify the effects of the filter time constant, initialization, load variation, and frequency estimation errors, and provide estimates of possible frequency-limit violations. We validate the proposed method on the IEEE 39-bus system using a high-fidelity electromagnetic-transient (EMT) model.

[Read the original at arXiv →](https://arxiv.org/abs/2611.34558v1)
