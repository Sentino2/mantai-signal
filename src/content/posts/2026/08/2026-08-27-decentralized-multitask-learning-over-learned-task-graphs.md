---
title: "Decentralized Multitask Learning over Learned Task Graphs"
date: 2026-08-27T11:37:11+00:00
source: "arXiv"
source_url: "https://arxiv.org/abs/2608.26989v1"
tags: ["hardware", "security"]
summary: "This paper investigates decentralized multitask learning over networks when the underlying task relationships are unknown. While existing graph-regularized multitask frameworks typically assume a known structure, practical settings often require learning inter-task dependencies directly from distributed data. We propose a decentralized two-phase strategy that first estimates a generalized graph La"
---

This paper investigates decentralized multitask learning over networks when the underlying task relationships are unknown. While existing graph-regularized multitask frameworks typically assume a known structure, practical settings often require learning inter-task dependencies directly from distributed data. We propose a decentralized two-phase strategy that first estimates a generalized graph Laplacian from noisy non-cooperative stochastic gradient iterates, and subsequently exploits the learned graph to enable cooperative multitask diffusion learning. This framework is motivated by a Gaussian Markov random field prior, which gives rise to a decentralized maximum likelihood estimator for the graph Laplacian. The analysis quantifies the Laplacian estimation error and its propagation to the steady-state performance of the multitask diffusion recursion, and introduces a topology sensitivity index to capture the effect of network heterogeneity. Simulation results corroborate the theoretical findings and demonstrate that cooperation enabled by the learned task graph significantly improves performance over non-cooperative learning, while approaching the true-graph baseline when the estimation stepsize is sufficiently small.

[Read the original at arXiv →](https://arxiv.org/abs/2608.26989v1)
