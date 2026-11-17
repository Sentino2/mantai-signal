---
title: "Warm Starting Neural Dynamics Models From Few Jacobian Samples"
date: 2026-11-16T17:46:39+00:00
source: "arXiv"
source_url: "https://arxiv.org/abs/2611.21465v1"
ext_id: "arxiv:2611.21465v1"
tags: ["hardware", "models"]
summary: "Model-based reinforcement learning (MBRL) leverages a model of the environment, used for planning and generating samples without interacting with the real world. Motivated by evidence that informed initialization significantly improves the efficiency of MBRL, we propose TDec-Init, an algorithm to warm-start neural dynamics models using transition Jacobians. Using a decoupling algorithm based on th"
---

Model-based reinforcement learning (MBRL) leverages a model of the environment, used for planning and generating samples without interacting with the real world. Motivated by evidence that informed initialization significantly improves the efficiency of MBRL, we propose TDec-Init, an algorithm to warm-start neural dynamics models using transition Jacobians. Using a decoupling algorithm based on the decomposition of a tensor of stacked Jacobian samples, we recover weights and flexible nonlinearities, and use them to initialize a feedforward neural network. In the low-data regime, we show on several benchmark environments that our approach outperforms random initialization and value training, and either matches or outperforms Sobolev training, while requiring fewer training steps between episodes.

[Read the original at arXiv →](https://arxiv.org/abs/2611.21465v1)
