---
title: "xTRUCE: A Provably Safe Arbiter for Multi-xApp Conflict Mitigation in Agentic O-RAN"
date: 2026-08-28T17:08:53+00:00
source: "arXiv"
source_url: "https://arxiv.org/abs/2608.28532v1"
tags: ["hardware", "models"]
summary: "The open radio access network (O-RAN) is evolving toward agentic operation, where large language model (LLM)-driven xApps/rApps generate control proposals under operator intents. However, such proposals may be conflicting, infeasible, or hallucinated, and no existing system jointly provides proposal-independent safety, priority-aware reconciliation, and traceable feedback. To this end, we propose "
---

The open radio access network (O-RAN) is evolving toward agentic operation, where large language model (LLM)-driven xApps/rApps generate control proposals under operator intents. However, such proposals may be conflicting, infeasible, or hallucinated, and no existing system jointly provides proposal-independent safety, priority-aware reconciliation, and traceable feedback. To this end, we propose a provably safe arbiter, namely xTRUCE, in the near-real-time (Near-RT) RAN intelligent controller for mitigating multi-xApp conflicts in gNB control. We first develop a structured xApp proposal interface and a three-layer constraint hierarchy that places physical limits and operator-defined rules above relaxable performance targets, alongside a dual-timescale control action space. A two-stage arbitration mechanism then minimizes target shortfalls in the operator-priority order to finalize safe E2 actions within the Near-RT latency budget, while returning conflict certificates to xApps and the operator for renegotiation. Finally, we implement xTRUCE in a multi-cell O-RAN use case, and evaluate its multi-process prototype through simulations with live API-backed LLM xApps and over-the-air experiments on OpenAirInterface/FlexRIC-based O-RAN stacks. Results show that xTRUCE ensures gNB control safety with $100\%$ protected services despite severe proposal hallucinations, achieves priority-consistent performance satisfaction under overload, efficiently guides LLM intent renegotiation via certificates, and keeps a delay-safe E2 control loop.

[Read the original at arXiv →](https://arxiv.org/abs/2608.28532v1)
