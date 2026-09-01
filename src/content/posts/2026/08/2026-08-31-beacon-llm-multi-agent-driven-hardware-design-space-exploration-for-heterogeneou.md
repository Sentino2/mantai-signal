---
title: "Beacon: LLM Multi-Agent Driven Hardware Design Space Exploration for Heterogeneous Multi-Chiplet Deep Learning Accelerators"
date: 2026-08-31T15:07:15+00:00
source: "arXiv"
source_url: "https://arxiv.org/abs/2608.30932v1"
tags: ["models"]
summary: "Heterogeneous multi-chiplet accelerators allow chiplets to be configured independently to better match different operator characteristics and improve inference efficiency. However, heterogeneity makes simulator evaluation expensive, limiting the number of iterations affordable for hardware design space exploration (HW-DSE). Mainstream data-driven methods rely mainly on final metrics and a few pred"
---

Heterogeneous multi-chiplet accelerators allow chiplets to be configured independently to better match different operator characteristics and improve inference efficiency. However, heterogeneity makes simulator evaluation expensive, limiting the number of iterations affordable for hardware design space exploration (HW-DSE). Mainstream data-driven methods rely mainly on final metrics and a few predefined states, and require many search iterations to implicitly learn the relationships between input parameters and optimization objectives, making them less effective in this setting. In practice, evaluators also generate detailed reports on execution timelines, resource utilization, memory accesses, and communication behavior. Large language models (LLMs) can combine domain knowledge with these reports to explicitly identify bottleneck locations, degradation causes, and parameter adjustment directions, thereby improving each design decision under limited iteration budgets. Based on this observation, we propose Beacon, a report-driven LLM multi-agent framework for heterogeneous multi-chiplet HW-DSE. Beacon employs hierarchical agents for bottleneck localization, root-cause diagnosis, and hardware candidate generation, together with an Analysis Toolbox and RAG memory for closed-loop search. Under the same limited iteration budget, Beacon reduces the composite latency-energy-monetary-cost objective by 25.1\%--93.5\% compared with random search, Bayesian optimization, and reinforcement learning.

[Read the original at arXiv →](https://arxiv.org/abs/2608.30932v1)
