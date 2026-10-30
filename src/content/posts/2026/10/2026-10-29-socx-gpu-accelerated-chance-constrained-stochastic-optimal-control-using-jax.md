---
title: "socx: GPU-Accelerated Chance-Constrained Stochastic Optimal Control using JAX"
date: 2026-10-29T16:50:11+00:00
source: "arXiv"
source_url: "https://arxiv.org/abs/2610.40427v1"
ext_id: "arxiv:2610.40427v1"
tags: ["hardware", "security"]
summary: "In this article, we present socx, a GPU-accelerated solver for lifted convex reformulations of linear stochastic optimal control under chance constraints, implemented in JAX. We demonstrate that by exploiting the sparse and independent structure of the problem, distributed optimization can reduce it to simpler problems: independent linear-quadratic tracking (LQT) problems and Euclidean projections"
---

In this article, we present socx, a GPU-accelerated solver for lifted convex reformulations of linear stochastic optimal control under chance constraints, implemented in JAX. We demonstrate that by exploiting the sparse and independent structure of the problem, distributed optimization can reduce it to simpler problems: independent linear-quadratic tracking (LQT) problems and Euclidean projections onto sets. These simpler problems can be solved in parallel and then coupled using the constraints. To validate our solver, we run it on a hover-linearized 3D quadrotor and show a speed-up of up to $98\times$ over MOSEK and up to $2224\times$ over SCS. socx also solves horizons up to $N=1120$, whereas MOSEK runs out of memory at $N=320$. We present ablations to isolate the key components that enable the speed-up.

[Read the original at arXiv →](https://arxiv.org/abs/2610.40427v1)
