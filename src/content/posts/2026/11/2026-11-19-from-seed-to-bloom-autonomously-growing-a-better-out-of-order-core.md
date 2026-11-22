---
title: "From Seed to BLOOM: Autonomously Growing a Better Out-of-Order Core"
date: 2026-11-19T17:59:02+00:00
source: "arXiv"
source_url: "https://arxiv.org/abs/2611.26517v1"
ext_id: "arxiv:2611.26517v1"
tags: ["models"]
summary: "Improving microprocessor performance while meeting ASIC implementation constraints like area and frequency is a complex and labor-intensive task that requires expertise across computer architecture, hardware design, and performance analysis and profiling. While large teams in industry can afford the engineering resources to target this problem across performance modeling, RTL design, and ASIC impl"
---

Improving microprocessor performance while meeting ASIC implementation constraints like area and frequency is a complex and labor-intensive task that requires expertise across computer architecture, hardware design, and performance analysis and profiling. While large teams in industry can afford the engineering resources to target this problem across performance modeling, RTL design, and ASIC implementations, small teams of researchers and engineers cannot take on this huge engineering burden while keeping up with the pace of advancement in processor microarchitecture. Recent advancements in large language model (LLM) agents present a promising substrate to accelerate this traditionally human-intensive process.   In this work, we build and evaluate MiracleGro, an agentic AI-based system that, without human intervention, analyzes cycle-level RTL behavior and synthesis results, identifies performance bottlenecks, and translates architectural ideas into RTL implementation in a leading open-source out-of-order superscalar application core, the Berkeley Out-of-Order Machine (BOOM). Taking into account cycle-exact performance, area, and critical path, MiracleGro automatically produces improved BOOM designs that drastically increase the human-optimized BOOM's performance on substantial workload suites such as SPEC CPU2017 with full reference inputs.   MiracleGro achieves an 85% IPC speedup and a frequency improvement of 27% in SkyWater 130nm, resulting in a 2.34x wall-clock time speedup on the full SPEC CPU2017 intspeed benchmarks (30 trillion instructions). This result demonstrates the enormous opportunity to harness frontier models to improve state-of-the-art RTL-driven platforms for implementation-grounded microarchitecture research across hardware designs.

[Read the original at arXiv →](https://arxiv.org/abs/2611.26517v1)
