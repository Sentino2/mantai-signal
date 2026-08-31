---
title: "Scalable Voltage-Stability Dataset Generation Via Boundary-Proximity Indicators Clustering"
date: 2026-08-28T13:02:10+00:00
source: "arXiv"
source_url: "https://arxiv.org/abs/2608.28298v1"
tags: ["hardware"]
summary: "This paper proposes a scalable framework for voltage-stability dataset generation. Voltage-stability-constrained planning increasingly relies on machine-learning surrogates but training them requires large datasets labelled by continuation power flow (CPF) results, which is computationally costly. To address this, this paper proposes a framework that uses hierarchical clustering on boundary-proxim"
---

This paper proposes a scalable framework for voltage-stability dataset generation. Voltage-stability-constrained planning increasingly relies on machine-learning surrogates but training them requires large datasets labelled by continuation power flow (CPF) results, which is computationally costly. To address this, this paper proposes a framework that uses hierarchical clustering on boundary-proximity indicators to reduce the number of required CPF evaluations. The proposed approach combines (i) uniform sampling of feasible operating space using Hit-and-Run Markov Chain Monte Carlo, (ii) structured stress directions via maximin Latin hypercube sampling (LHS), (iii) sensitivity-guided perturbations to target weak buses, and (iv) clustering-based representative CPF labelling that reconstructs the voltage stability margins of unlabelled operating points from representative cluster medoids. Results on the IEEE 39-bus system show that the proposed framework significantly reduces CPF evaluations by 95.45% while preserving high accuracy and boundary fidelity for both regression and classification tasks. The reduced surrogates remain structurally consistent with their full-CPF dataset counterparts, demonstrating the suitability and scalability of the proposed approach for operation and planning optimization.

[Read the original at arXiv →](https://arxiv.org/abs/2608.28298v1)
