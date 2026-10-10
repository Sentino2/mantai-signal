---
title: "Adaptive dynamic programming using Lyapunov function constraints"
date: 2026-10-08T15:07:08+00:00
source: "arXiv"
source_url: "https://arxiv.org/abs/2610.12110v1"
ext_id: "arxiv:2610.12110v1"
tags: ["hardware"]
summary: "This work is concerned with a stabilizing adaptive dynamic programming (ADP) approach to approximate solution of a given infinite-horizon optimal control problem. Since the latter problem cannot, in general, be solved exactly, a parametrized function approximator for the infinite-horizon cost function is introduced in ADP (so called ``critic''). This critic is used to adapt the parameters of the f"
---

This work is concerned with a stabilizing adaptive dynamic programming (ADP) approach to approximate solution of a given infinite-horizon optimal control problem. Since the latter problem cannot, in general, be solved exactly, a parametrized function approximator for the infinite-horizon cost function is introduced in ADP (so called ``critic''). This critic is used to adapt the parameters of the function approximator. The so called ``actor'' in turn derives the optimal input of the system. It is a notoriously hard problem to guarantee closed-loop stability of ADP due to the use of approximation structures in the control scheme. Since at least stabilizability is always assumed in the analyses of ADP, it is justified to invoke a respective Lyapunov function. The proposed ADP scheme explicitly uses the said Lyapunov function to simultaneously optimize the critic and guarantee closed-loop stability. A Hessian-free optimization routine is utilized for the actor and critic optimization problems. Convergence to prescribed vicinities of the optima is shown. A computational study showed significant performance improvement for the critic-based approach compared a nominal stabilizing controller for a range of initial conditions.

[Read the original at arXiv →](https://arxiv.org/abs/2610.12110v1)
