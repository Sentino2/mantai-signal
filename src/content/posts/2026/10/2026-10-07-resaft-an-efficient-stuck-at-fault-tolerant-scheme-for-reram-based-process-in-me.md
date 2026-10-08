---
title: "ReSAFT: An Efficient Stuck-at Fault-Tolerant Scheme for ReRAM-based Process-in-Memory Accelerators"
date: 2026-10-07T12:56:03+00:00
source: "arXiv"
source_url: "https://arxiv.org/abs/2610.09999v1"
ext_id: "arxiv:2610.09999v1"
tags: ["models"]
summary: "Analog ReRAM-based process-in-memory (PIM) accelerators provide high parallelism and energy efficiency for deep convolutional neural networks (CNNs) inference. However, their susceptibility to permanent faults, such as stuck-at high (SaH) and stuck-at low (SaL) resistance states, poses a major challenge by permanently corrupting the CNN weights mapped to conductance values of ReRAM cells and degra"
---

Analog ReRAM-based process-in-memory (PIM) accelerators provide high parallelism and energy efficiency for deep convolutional neural networks (CNNs) inference. However, their susceptibility to permanent faults, such as stuck-at high (SaH) and stuck-at low (SaL) resistance states, poses a major challenge by permanently corrupting the CNN weights mapped to conductance values of ReRAM cells and degrading inference accuracy, which leads to system unreliability in safety-critical applications. In this paper, we propose a fault-tolerant scheme for analog ReRAM-based PIM accelerators to tackle stuck-at faults (SAFs) with minimal redundancy overhead to recover classification accuracy degradation. The proposed scheme contains a redundancy-based hardware solution alongside fault-aware mapping method for ensuring reliable analog computation in ReRAM crossbar. We analyze the impact of varying number of redundant rows and columns on accuracy and design metrics. Subsequently, a multi-objective optimization (MOO) problem is formulated and solved to efficiently determine the number of redundant rows and columns, considering trade-offs among various design metrics. Furthermore, a fault-aware weight mapping is proposed for dual-crossbar structures to further compensate for the accuracy degradation caused by SAFs. Simulation results show that, for the SimpleNet model using the MNIST dataset, the inference accuracy is recovered by approximately 22.39%, on average, across four configurations of optimal solutions, each offering a trade-off between reliability and area, energy consumption, and latency overheads. The mean-time-tofailure (MTTF) improves by about 61x on average compared to the baseline. These selected configurations also reduce energy and area overheads by 32%, on average, in comparison to row-only and column-only configurations.

[Read the original at arXiv →](https://arxiv.org/abs/2610.09999v1)
