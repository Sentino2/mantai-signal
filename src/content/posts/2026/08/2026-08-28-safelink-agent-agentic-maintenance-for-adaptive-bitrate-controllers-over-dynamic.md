---
title: "SafeLink-Agent: Agentic Maintenance for Adaptive Bitrate Controllers over Dynamic Starlink Networks"
date: 2026-08-28T11:08:40+00:00
source: "arXiv"
source_url: "https://arxiv.org/abs/2608.28194v1"
tags: ["hardware", "models"]
summary: "Low Earth orbit (LEO) satellite broadband, represented by Starlink, is making high-resolution video streaming feasible beyond fixed terrestrial coverage. However, Starlink access links change across time and regions, exposing adaptive bitrate (ABR) streaming to shifting throughput tails, latency, volatility, and handover conditions. Existing ABR controllers are usually designed, tuned, or trained "
---

Low Earth orbit (LEO) satellite broadband, represented by Starlink, is making high-resolution video streaming feasible beyond fixed terrestrial coverage. However, Starlink access links change across time and regions, exposing adaptive bitrate (ABR) streaming to shifting throughput tails, latency, volatility, and handover conditions. Existing ABR controllers are usually designed, tuned, or trained for specific network conditions, making it difficult to handle newly exposed hard Starlink profiles. This paper proposes SafeLink-Agent, an agentic maintenance framework for ABR controllers over dynamic Starlink networks. SafeLink-Agent summarizes exposed failures and uses a large language model (LLM)-based agentic patch proposer to generate candidate patches, while replay verification determines whether each patch can be safely committed. The framework supports both rule-based controllers and learned controllers under the same maintenance workflow. Experiments on real Starlink networks show that SafeLink-Agent reduces the severe-session ratio of RobustMPC from 2.60% to 0.40% and reduces cumulative severe sessions from 45 to 7 in rolling maintenance. For learned controllers, verified adaptive auditing lowers the average severe-session ratio from 39.01% to 9.79%. These results demonstrate that agentic maintenance can improve ABR robustness under dynamic Starlink access conditions.

[Read the original at arXiv →](https://arxiv.org/abs/2608.28194v1)
