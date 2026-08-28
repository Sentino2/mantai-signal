---
title: "Adversarially-Informed Node Criticality Identification in Power Grid Measurements"
date: 2026-08-27T17:24:46+00:00
source: "arXiv"
source_url: "https://arxiv.org/abs/2608.27393v1"
tags: ["hardware", "industrial", "security"]
summary: "Power grid state estimation relies on sensor measurements that are increasingly vulnerable to adversarial corruption in cyberphysical environments, potentially leading to significant deviations in system observations. This motivates the need to identify critical measurement nodes whose compromise results in the most severe system-level impact. However, existing node criticality methods primarily r"
---

Power grid state estimation relies on sensor measurements that are increasingly vulnerable to adversarial corruption in cyberphysical environments, potentially leading to significant deviations in system observations. This motivates the need to identify critical measurement nodes whose compromise results in the most severe system-level impact. However, existing node criticality methods primarily rely on structural or steady-state analyses and do not explicitly account for adversarial effects on system behavior. To address this gap, this paper proposes an adversarially informed framework for identifying critical measurement nodes in linearized power systems. Within this framework, a structured attack generation mechanism is developed to construct stealthy and effective false data injection attacks (FDIAs) against an H-infinity resilient state estimator. Node criticality is then evaluated using coalition-based marginal contributions of compromised sensor subsets, estimated via permutation sampling over a prescribed set of admissible nodes, with the resulting importance scores mapped to the corresponding physical buses. Simulation results on the IEEE 14-bus system show that adversarially identified nodes induce larger deviations in frequency, voltage angle, and net power compared to randomly selected nodes, demonstrating the effectiveness of the proposed framework.

[Read the original at arXiv →](https://arxiv.org/abs/2608.27393v1)
