---
title: "Succinct Infinite-Horizon Lyapunov and LQR Value Problems Are BQP-Complete"
date: 2026-11-09T17:36:55+00:00
source: "arXiv"
source_url: "https://arxiv.org/abs/2611.12757v1"
ext_id: "arxiv:2611.12757v1"
tags: ["hardware"]
summary: "Fundamental tasks in linear systems analysis and control require evaluating infinite-horizon output energies for autonomous systems and optimal value functions for controlled systems. These quantities are characterized by Lyapunov and algebraic Riccati equations, respectively. In this work, we study promise problems for their evaluation when the system matrices are sparse and represented succinctl"
---

Fundamental tasks in linear systems analysis and control require evaluating infinite-horizon output energies for autonomous systems and optimal value functions for controlled systems. These quantities are characterized by Lyapunov and algebraic Riccati equations, respectively. In this work, we study promise problems for their evaluation when the system matrices are sparse and represented succinctly by Boolean circuits specifying their nonzero entries, with input length polynomial in the logarithm of the system dimension. For dissipative autonomous systems with coordinate-vector initial states, we define the succinct Lyapunov value problem (SLV). Its extension to linear-quadratic optimal control is the succinct LQR value problem (SLQRV). We prove that SLV is $\BQP$-hard: every problem in bounded-error quantum polynomial time ($\BQP$) reduces to it in polynomial time. We then establish that the more general SLQRV problem admits a quantum algorithm running in time polynomial in the succinct input length. Since SLV is a special case of SLQRV, both problems are $\BQP$-complete. Consequently, unless bounded-error probabilistic polynomial time coincides with $\BQP$, no classical randomized algorithm can solve either problem on all promised instances in time polynomial in the succinct input length.

[Read the original at arXiv →](https://arxiv.org/abs/2611.12757v1)
