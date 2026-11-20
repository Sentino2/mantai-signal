---
title: "Learning Control-Relevant Koopman Representations from Input-Output Trajectories"
date: 2026-11-19T18:26:11+00:00
source: "arXiv"
source_url: "https://arxiv.org/abs/2611.26559v1"
ext_id: "arxiv:2611.26559v1"
tags: ["hardware", "models"]
summary: "Predictive accuracy alone does not ensure that data-driven Koopman representations are suitable for output-feedback control. This paper develops a continuous-time framework for learning control-relevant Koopman representations using only measured input-output trajectories. A causal encoder constructs the lifted state from a finite input-output window, and an additive lifted model is identified by "
---

Predictive accuracy alone does not ensure that data-driven Koopman representations are suitable for output-feedback control. This paper develops a continuous-time framework for learning control-relevant Koopman representations using only measured input-output trajectories. A causal encoder constructs the lifted state from a finite input-output window, and an additive lifted model is identified by integral regression. We distinguish observability, input-map compatibility, controllability, and data informativity. We characterize compatibility with a constant lifted input matrix, quantify input-map mismatch, and, under exact lifting assumptions, relate iterated Lie brackets to the controllable subspace of the lifted realization. A covariance-normalized finite-horizon observability criterion is optimized subject to separate bounds on output-prediction and temporal-consistency errors. Under the stated exactness and observability assumptions, the encoded lifted state depends only on the current nonlinear state. For approximate representations, we bound the difference between encodings of distinct past trajectories ending at the same state. An exactly liftable controlled system provides analytical ground truth, while a controlled Duffing oscillator illustrates the approximate setting, for which an informative exact additive lifting on an open set is shown to be impossible. On the exact benchmark, encoder initialization determines whether the learned representation recovers the analytical lift. In the reported Duffing experiments, observability promotion improves nominal Gramian measures without improving observer-based estimation or tracking, while updating the lifted-state estimate through the encoder at every sampling instant has a larger effect on tracking accuracy.

[Read the original at arXiv →](https://arxiv.org/abs/2611.26559v1)
