---
title: "Timing-Driven Logic Remapping with Local Physical Context"
date: 2026-10-01T15:56:10+00:00
source: "arXiv"
source_url: "https://arxiv.org/abs/2610.01918v1"
ext_id: "arxiv:2610.01918v1"
tags: ["models"]
summary: "The timing behavior of a mapped circuit depends on both its logic implementation and the physical environment in which that implementation is realized. Revisiting mapping decisions after placement therefore requires a search procedure that accounts for surrounding timing constraints, fanout loads, and interconnect effects. We study local remapping in this setting and develop a framework that coupl"
---

The timing behavior of a mapped circuit depends on both its logic implementation and the physical environment in which that implementation is realized. Revisiting mapping decisions after placement therefore requires a search procedure that accounts for surrounding timing constraints, fanout loads, and interconnect effects. We study local remapping in this setting and develop a framework that couples discrete mapping search with physical implementation feedback. Timing-critical regions are isolated through bounded windows whose interfaces retain the context of the surrounding circuit. Within each window, a mixed-integer formulation jointly selects logic cuts, signal polarities, and library cells under a delay model informed by estimated locations and interconnect parasitics. A continuous relaxation filters the search space before discrete optimization produces alternative implementations with similar modeled timing and different structural choices. These implementations are reconstructed and assessed through legalization, routing-based parasitic estimation, and timing analysis. Physically validated improvements are incorporated into the design, and the updated context guides subsequent searches. The framework provides a systematic way to revisit local logic implementations while accounting for their interaction with an existing placement.

[Read the original at arXiv →](https://arxiv.org/abs/2610.01918v1)
