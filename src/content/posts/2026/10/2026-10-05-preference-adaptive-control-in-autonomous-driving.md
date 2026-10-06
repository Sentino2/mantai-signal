---
title: "Preference-Adaptive Control in Autonomous Driving"
date: 2026-10-05T15:37:50+00:00
source: "arXiv"
source_url: "https://arxiv.org/abs/2610.06539v1"
ext_id: "arxiv:2610.06539v1"
tags: ["hardware", "models"]
summary: "In this paper, we present a preference-adaptive receding-horizon control framework for autonomous driving that accounts for passenger preferences and motion-sickness susceptibility. We formulate a finite-horizon optimal control problem with adaptive weights for speed, acceleration comfort, and motion sickness, while maintaining a fixed weight for collision risk. We predict motion sickness online u"
---

In this paper, we present a preference-adaptive receding-horizon control framework for autonomous driving that accounts for passenger preferences and motion-sickness susceptibility. We formulate a finite-horizon optimal control problem with adaptive weights for speed, acceleration comfort, and motion sickness, while maintaining a fixed weight for collision risk. We predict motion sickness online using an individualized model on the Motion Illness Symptoms Classifi- cation (MISC) scale and update the preference weights offline from emotion-derived pairwise comparisons using Bayesian inference. A deterministic safety supervisor checks the planned trajectory and modifies the control command when necessary. We evaluate the framework using three simulated passenger profiles under three motion-sickness susceptibility levels. The learned weights yield distinct closed-loop behaviors, and the mean evaluation emotion score improves in seven of nine scenarios. No collisions occur in the full-method experiments, while the safety supervisor intervenes in 1.621% of the learning frames.

[Read the original at arXiv →](https://arxiv.org/abs/2610.06539v1)
