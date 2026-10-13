---
title: "Hierarchical Graph Neural Network for Probabilistic Power Flow with Grid Topology Contingencies"
date: 2026-10-09T12:27:41+00:00
source: "arXiv"
source_url: "https://arxiv.org/abs/2610.13495v1"
ext_id: "arxiv:2610.13495v1"
tags: ["hardware", "industrial", "models"]
summary: "Data-driven surrogates reduce the nonlinear solves required for probabilistic power flow (PPF), but models tied to a fixed bus--branch graph often generalize poorly when outages change electrical coupling. This paper proposes a topology-decomposition-driven hierarchical bidirectional graph neural network (TDD--HBGNN) for PPF under unseen topologies. For each realized topology, the network is decom"
---

Data-driven surrogates reduce the nonlinear solves required for probabilistic power flow (PPF), but models tied to a fixed bus--branch graph often generalize poorly when outages change electrical coupling. This paper proposes a topology-decomposition-driven hierarchical bidirectional graph neural network (TDD--HBGNN) for PPF under unseen topologies. For each realized topology, the network is decomposed into fundamental topological units (FTUs), dynamically homogeneous voltage clusters (DHVCs), and a core backbone sub-grid (CBSG), with equivalent-admittance representations preserving electrical ports between units. A sensitivity-based linear prior captures the first-order voltage-magnitude and phase-angle response, while the HBGNN learns topology-dependent nonlinear residuals. Impedance- and uncertainty-aware bottom-up aggregation condenses local perturbations, while mode-modulated top-down broadcasting restores system context at buses. We evaluate our approach on the IEEE 118-bus and Polish 2746-bus systems under unseen N--1 and N--2 contingencies against six baseline methods. Compared with these methods, TDD--HBGNN achieves 2.47--4.20-fold lower all-bus phase-angle errors and lower phase-angle errors in every held-out event. Its voltage-magnitude advantage is concentrated near the outaged branches, where paired error ratios reach 1.75--2.58 on the IEEE system and 1.87--1.97 in Polish N--2 events. All system--contingency--baseline comparisons favor TDD--HBGNN in joint voltage--angle error. Moreover, shared hierarchical operators keep the model size at 0.658 million parameters across both grids and yield 0.161--1.793~ms forward latency per probabilistic case. These results demonstrate system-wide angular accuracy, outage-local voltage accuracy, and parameter-efficient scaling across unseen topologies.

[Read the original at arXiv →](https://arxiv.org/abs/2610.13495v1)
