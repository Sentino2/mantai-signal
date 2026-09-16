---
title: "RobResilience: Implementing and Evaluating a Resilience Framework for Cyber-Physical Embodied Systems"
date: 2026-09-15T15:49:04+00:00
source: "arXiv"
source_url: "https://arxiv.org/abs/2609.17349v1"
ext_id: "arxiv:2609.17349v1"
tags: ["hardware", "security"]
summary: "In embodied cyber-physical systems, active cyberattacks pose an immediate threat not just to data, but to physical integrity and human safety. While existing security approaches excel at detection, they lack the runtime mechanisms to determine whether a disruption is tolerable or if performance degradation remains within safe operational bounds. This gap leaves autonomous systems vulnerable to gra"
---

In embodied cyber-physical systems, active cyberattacks pose an immediate threat not just to data, but to physical integrity and human safety. While existing security approaches excel at detection, they lack the runtime mechanisms to determine whether a disruption is tolerable or if performance degradation remains within safe operational bounds. This gap leaves autonomous systems vulnerable to graceful failure paralysis, where they cannot distinguish between a safe, degraded state and a catastrophic hazard during an ongoing attack. This paper presents RobResilience, an implementation of a formal resilience framework for embodied cyber-physical systems in a Webots simulation environment, using a PR2 robot and ROS2. The framework evaluates three predicates at runtime: tolerable disruption ($δ$), tolerable degradation ($γ$), and mitigation feasibility ($μ$), over a compromised device set derived from IDS confidence scores. When resilience is lost, the framework triggers available mitigation strategies. We evaluate our implementation through eight attack scenarios that systematically cover all possible combinations of the predicate state space, varying attack targets, degradation rates, and mitigation availability. Results confirm that the runtime behaviour of the implementation is consistent with the theoretical definitions.

[Read the original at arXiv →](https://arxiv.org/abs/2609.17349v1)
