---
title: "Statistical Learning of Contractive Dynamical Representations for Composite Adaptive Control"
date: 2026-09-28T17:59:07+00:00
source: "arXiv"
source_url: "https://arxiv.org/abs/2609.35758v1"
ext_id: "arxiv:2609.35758v1"
tags: ["hardware", "models"]
summary: "We present a representation-learning framework for composite adaptive tracking control under dynamically coupled disturbances. The framework connects classical disturbance-accommodating control (DAC) to recent last-layer adaptive disturbance-rejection methods. Specifically, we introduce a statistically principled hard expectation-maximization (hard-EM) procedure, with a Kalman smoother in the hard"
---

We present a representation-learning framework for composite adaptive tracking control under dynamically coupled disturbances. The framework connects classical disturbance-accommodating control (DAC) to recent last-layer adaptive disturbance-rejection methods. Specifically, we introduce a statistically principled hard expectation-maximization (hard-EM) procedure, with a Kalman smoother in the hard E-step, to identify dynamical representations of disturbance whose latent evolution is uniformly contractive. The learned representation evolves a latent disturbance-excitation state from measured plant features and control inputs and decodes that state into the time-varying disturbance acting on the nominal plant, thereby extending prior "fixed-decay" last-layer adaptive methods to a learned, predictive DAC-style formulation. Combined with Bayesian filtering of the learned latent state, this representation yields a composite adaptive tracking controller with predictive capability and provable exponential convergence to a bounded neighborhood. We validate our approach experimentally on a slippery ground vehicle carrying a liquid-sloshing tank and a pendulum load, and we further assess its robustness on a system of coupled Duffing oscillators. Across both settings, the method achieves accurate disturbance prediction and improved overall tracking performance relative to fixed-decay representation-learning ablations, LTI disturbance-accommodating baselines, and model-based PD baselines.

[Read the original at arXiv →](https://arxiv.org/abs/2609.35758v1)
