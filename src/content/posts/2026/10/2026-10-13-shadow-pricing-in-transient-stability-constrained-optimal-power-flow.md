---
title: "Shadow Pricing in Transient Stability-Constrained Optimal Power Flow"
date: 2026-10-13T15:33:00+00:00
source: "arXiv"
source_url: "https://arxiv.org/abs/2610.18563v1"
ext_id: "arxiv:2610.18563v1"
tags: ["hardware"]
summary: "Transient stability constraints alter the economic dispatch of power systems, while the resulting price signals and their implications for market settlement remain insufficiently characterized. Existing approaches identify stability-related components in locational marginal prices, without deriving shadow prices for individual assets, such as generators and loads, or analyzing the resulting settle"
---

Transient stability constraints alter the economic dispatch of power systems, while the resulting price signals and their implications for market settlement remain insufficiently characterized. Existing approaches identify stability-related components in locational marginal prices, without deriving shadow prices for individual assets, such as generators and loads, or analyzing the resulting settlement. To address this gap, this paper derives shadow prices from a transient stability-constrained optimal power flow in which the differential-algebraic equations governing the system dynamics are embedded through direct discretization. Each shadow price decomposes into a nodal energy component and a stability component, the latter formed by the dual variables of the dynamic equations in which the power of the asset appears. Shadow prices are therefore asset-specific: co-located generators and loads are assigned the same nodal energy component, but can be subject to different stability components when their transient behaviors differ. Case studies on the WECC 9-bus system and a modified IEEE 39-bus system show that settlement at the proposed shadow prices allocates the cost of the stability constraints among the assets without any side payment. An asset that reduces the stability margin is charged its stability component, whereas an asset that improves it is paid, and no generator is dispatched at a loss.

[Read the original at arXiv →](https://arxiv.org/abs/2610.18563v1)
