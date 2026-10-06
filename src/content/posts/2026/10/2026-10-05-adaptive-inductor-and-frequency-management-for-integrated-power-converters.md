---
title: "Adaptive Inductor and Frequency Management for Integrated Power Converters"
date: 2026-10-05T15:46:40+00:00
source: "arXiv"
source_url: "https://arxiv.org/abs/2610.06555v1"
ext_id: "arxiv:2610.06555v1"
tags: ["hardware"]
summary: "This work presents a digitally controlled adaptive power conversion framework that dynamically co-optimizes inductor configuration and switching frequency to achieve high efficiency across a wide range of load conditions. Conventional buck converters are typically optimized for a single operating point, leading to efficiency degradation under dynamic loads due to mismatches between inductance, swi"
---

This work presents a digitally controlled adaptive power conversion framework that dynamically co-optimizes inductor configuration and switching frequency to achieve high efficiency across a wide range of load conditions. Conventional buck converters are typically optimized for a single operating point, leading to efficiency degradation under dynamic loads due to mismatches between inductance, switching frequency, and load current. To address this limitation, a reconfigurable inductor architecture is proposed. With this approach, the effective inductance and switching frequency are adjusted at runtime with on-chip digital controller. An end-to-end design methodology is developed, integrating physics-based analytical modeling, finite element method (FEM) simulations, and an optimization framework to determine preferred operating points across the load range. The resulting configurations are stored in a lookup table and implemented in real time through a low-overhead control scheme. The system explicitly accounts for both inductor and switching device losses, enabling co-optimization of conduction and switching losses within current ripple and continuous conduction mode (CCM) constraints. To ensure robust operation under fast load transients, a hysteresis-based control strategy is introduced to mitigate temporary CCM violations caused by sensing latency. An entry-margin condition is derived under which continuous conduction is guaranteed for a bounded load slew rate. Simulation results demonstrate a 4.5 percentage-point improvement in average efficiency and up to a 32% reduction in average power loss relative to fixed configurations, highlighting the effectiveness of adaptive inductance-frequency management in integrated power delivery systems with dynamic load profiles.

[Read the original at arXiv →](https://arxiv.org/abs/2610.06555v1)
