---
title: "FAITH: Feasibility-Aware Safety-Filtered RL for High-Dimensional Systems"
date: 2026-10-08T17:57:06+00:00
source: "arXiv"
source_url: "https://arxiv.org/abs/2610.12432v1"
ext_id: "arxiv:2610.12432v1"
tags: ["hardware", "models"]
summary: "Safe reinforcement learning commonly places safety and task performance in the same policy objective, where they can introduce competing updates. Safety filters separate them at action execution, but classical designs require an analytic safety function and dynamics model, and standard minimal-intervention filters are myopic to long-horizon task return because they minimize only instantaneous acti"
---

Safe reinforcement learning commonly places safety and task performance in the same policy objective, where they can introduce competing updates. Safety filters separate them at action execution, but classical designs require an analytic safety function and dynamics model, and standard minimal-intervention filters are myopic to long-horizon task return because they minimize only instantaneous action deviation. Hard projections are also undefined when no safe action exists. We present FAITH, a feasibility-aware, model-free framework that approximates the optimal state-action safety value and amortizes minimal-intervention filtering with a feedforward network. The task policy optimizes the task return through the filtered dynamics, which recovers the feasible constrained problem without a competing safety term in the task-policy update. When no action satisfies the learned safety condition, the same filter approaches the action with minimum predicted peak harm. On a double integrator example and a Safety Gym environment, FAITH achieves the highest return among methods with no feasible-start violations and matches the lowest harm from infeasible starts. On a 29-DoF humanoid, it reaches a 99.95% safety rate while retaining 97% of the unfiltered return in Walking-Avoid, and obtains the highest measured safety rate in Push-Avoid by learning to sacrifice balancing and fall away from the protected region. The same policies are also demonstrated on a real-world Unitree G1 humanoid.

[Read the original at arXiv →](https://arxiv.org/abs/2610.12432v1)
