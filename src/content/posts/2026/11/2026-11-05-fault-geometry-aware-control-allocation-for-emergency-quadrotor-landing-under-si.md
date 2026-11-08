---
title: "Fault-Geometry-Aware Control Allocation for Emergency Quadrotor Landing under Single-Motor Loss of Effectiveness"
date: 2026-11-05T16:34:03+00:00
source: "arXiv"
source_url: "https://arxiv.org/abs/2611.08259v1"
ext_id: "arxiv:2611.08259v1"
tags: ["hardware", "models", "traction"]
summary: "Partial single-motor loss of effectiveness (LoE) changes the remaining control-authority geometry of a quadrotor and can change which control allocator performs best during emergency landing[cite: 11]. We compare three allocators in Crazyflie software-in-the-loop simulation: bounded weighted least squares (reported as PINV), a finite-candidate residual allocator (QP-lite), and the same residual al"
---

Partial single-motor loss of effectiveness (LoE) changes the remaining control-authority geometry of a quadrotor and can change which control allocator performs best during emergency landing[cite: 11]. We compare three allocators in Crazyflie software-in-the-loop simulation: bounded weighted least squares (reported as PINV), a finite-candidate residual allocator (QP-lite), and the same residual allocator with scoring parameters tuned offline by the Cross-Entropy Method (CEM)[cite: 11]. For this study, fault geometry is represented by the known failed-motor index[cite: 11]. At $η=0.496$ remaining effectiveness, matched development trials select CEM for M1, M3, and M4 and PINV for M2; the M3 selection is a one-trial margin (29/30 versus 28/30)[cite: 11]. After freezing this routing map, the policy achieves 117/120 safe first-contact touchdowns on fresh seeds and 115/120 in a separate randomized-order integrated-supervisor evaluation[cite: 11]. For the critical M2/PINV branch, Firth regression gives a nominal $η_{50}\approx0.4956$ with a within-model 95% bootstrap interval of approximately [0.4955, 0.4956][cite: 11]. One-factor-at-a-time $\pm10\%$ plant perturbations shift $η_{50}$ by up to 0.05495 for thrust coefficient and 0.04974 for mass; the most frequent violated first-contact criterion also changes from vertical speed in many conditions to angular rate for mass -10% and thrust-coefficient +10%[cite: 11]. At fixed $η=0.496$, PINV has a higher M2 safe count than frozen CEM in 9/11 tested plant states and ties in 2/11; the two ties are both 0/30[cite: 11]. The experiments therefore distinguish motor-conditioned allocator selection from sensitivity to plant-model mismatch[cite: 11].

[Read the original at arXiv →](https://arxiv.org/abs/2611.08259v1)
