---
title: "FedAvgIm: Federated Learning for Multi-Site Impedance Identification of Inverter-Based Resources"
date: 2026-10-26T15:50:11+00:00
source: "arXiv"
source_url: "https://arxiv.org/abs/2610.35640v1"
ext_id: "arxiv:2610.35640v1"
tags: ["hardware", "industrial", "models", "traction"]
summary: "With the increasing integration of inverter-based resources (IBRs) into power systems, assessing small-signal interaction stability has become essential. Impedance/admittance models enable frequency-domain characterization of IBR dynamics without requiring access to proprietary internal control details, but measurement-based identification is time-consuming and must be repeated across operating po"
---

With the increasing integration of inverter-based resources (IBRs) into power systems, assessing small-signal interaction stability has become essential. Impedance/admittance models enable frequency-domain characterization of IBR dynamics without requiring access to proprietary internal control details, but measurement-based identification is time-consuming and must be repeated across operating points. This paper proposes FedAvgIm, a privacy-aware federated-learning framework for multi-site dq-admittance identification under severe local data scarcity and raw-data-locality constraints. Each IBR site trains a local feed-forward neural network using a small set of operating-point-frequency samples, while only model parameters are shared with a cloud aggregator that performs sample-size-weighted FedAvg to update a global model and broadcast it back to all sites. To demonstrate effectiveness, EMT measurement-based admittance datasets are constructed for nine grid-following IBRs with different parameters, architectures, measurement-noise levels, and non-IID settings, where each client has only 40-390 training samples. Results show that FedAvgIm achieves performance close to centralized training and consistently outperforms local-only learning and raw-data-locality-preserving transfer-learning baselines. Additional studies show that FedAvgIm maintains stable learning behavior under measurement noise and remains beneficial under moderate non-IID conditions. The estimated dq-admittance models are further applied to generalized Nyquist stability analysis and validated against EMT time-domain simulations under multiple operating points and grid-strength conditions.

[Read the original at arXiv →](https://arxiv.org/abs/2610.35640v1)
