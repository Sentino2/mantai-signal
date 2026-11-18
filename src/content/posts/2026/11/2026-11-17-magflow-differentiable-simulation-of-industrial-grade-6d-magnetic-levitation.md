---
title: "Magflow: Differentiable Simulation of Industrial-Grade 6D Magnetic Levitation"
date: 2026-11-17T16:46:26+00:00
source: "arXiv"
source_url: "https://arxiv.org/abs/2611.23050v1"
ext_id: "arxiv:2611.23050v1"
tags: ["hardware", "models"]
summary: "Magnetic levitation with six-degrees-of-freedom enables frictionless transport and micrometer-scale positioning in principle, but low-level control is inherently challenging due to its complex and unstable dynamics. Industrial systems typically rely on deep hardware-software co-design, where mover and stator geometries are jointly designed to enable a compact, hand-crafted approximation of the ele"
---

Magnetic levitation with six-degrees-of-freedom enables frictionless transport and micrometer-scale positioning in principle, but low-level control is inherently challenging due to its complex and unstable dynamics. Industrial systems typically rely on deep hardware-software co-design, where mover and stator geometries are jointly designed to enable a compact, hand-crafted approximation of the electromagnetic force computation, thereby keeping control computationally tractable at kilohertz rates. However, this approach imposes overly conservative constraints on the operating workspace and the range of supported mover topologies. Instead of reducing the underlying physics to a hand-crafted approximation, we compute the physics directly. We introduce Magflow, a fully differentiable, GPU-parallel simulator for 6D magnetic levitation. It is used to train the first neural controller for an industrial-grade 6D magnetic levitation system that is learned purely from simulated physics. We show that the learned neural controller transfers zero-shot from simulation to real hardware while satisfying hard real-time constraints at 4 kHz. The learned controller achieves qualitatively new behaviors and even levitates a mover topology for which no hand-crafted solution exists. These results demonstrate that co-design is not a physical necessity for 6D magnetic levitation control. More broadly, control learning from simulated physics can find solutions beyond the reach of control engineering in demanding industrial domains. Source code and demonstration videos are publicly available at https://sites.google.com/view/magflow.

[Read the original at arXiv →](https://arxiv.org/abs/2611.23050v1)
