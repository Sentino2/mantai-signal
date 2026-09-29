---
title: "Adaptive Safety Filtering for Frozen ACC Policies via Conformal Residual Calibration"
date: 2026-09-28T15:29:42+00:00
source: "arXiv"
source_url: "https://arxiv.org/abs/2609.35415v1"
ext_id: "arxiv:2609.35415v1"
tags: ["hardware", "models"]
summary: "Frozen adaptive cruise control (ACC) policies can violate constraints when deployment dynamics differ from their training conditions. We propose residual-aware conformal action filtering (RACF), which calibrates residuals of a fixed nominal predictor and converts their quantile into an operating margin for finite-model action projection. Completed transitions update margins and candidate selection"
---

Frozen adaptive cruise control (ACC) policies can violate constraints when deployment dynamics differ from their training conditions. We propose residual-aware conformal action filtering (RACF), which calibrates residuals of a fixed nominal predictor and converts their quantile into an operating margin for finite-model action projection. Completed transitions update margins and candidate selection without retraining the policy. In a registered comparison over 2,400 controller-trial units, Adaptive RACF achieves 94.3% episode safety, improving by 19.9 percentage points over the evaluated nominal CBF-QP baseline while reducing projection frequency from 8.11% to 6.63%. A controlled study isolates a 4.54-point improvement from residual-margin injection. In a separate matched-hardware evaluation, Adaptive reduces mean amortized rollout time by 21.2% relative to Robust CBF-QP, with 161/180 versus 170/180 safe episodes. We characterize conditions linking one-step residual coverage to constraint satisfaction and quantify the observed safety-computation trade-offs.

[Read the original at arXiv →](https://arxiv.org/abs/2609.35415v1)
