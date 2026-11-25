---
title: "An exponential-rate consensus-based algorithms for estimation from relative measurements: implementation and performance analysis"
date: 2026-11-24T16:37:09+00:00
source: "arXiv"
source_url: "https://arxiv.org/abs/2611.32928v1"
ext_id: "arxiv:2611.32928v1"
tags: ["hardware"]
summary: "In this work we address the problem of optimal estimating the position of each agent in a network from relative noisy vectorial distances with its neighbors. Although the problem can be cast as a standard least-squares problem, the main challenge is to devise scalable algorithms that allow each agent to estimate its own position by means of only local communication and bounded complexity, independ"
---

In this work we address the problem of optimal estimating the position of each agent in a network from relative noisy vectorial distances with its neighbors. Although the problem can be cast as a standard least-squares problem, the main challenge is to devise scalable algorithms that allow each agent to estimate its own position by means of only local communication and bounded complexity, independently of the network size and topology. We first propose a synchronous consensus-based algorithm that is guaranteed to have exponentially convergence rate to the optimal centralized least-squares solution. We then extend this algorithm to more realistic asynchronous implementations via the use of local memory variables. We show that exponential convergence is still guaranteed under both uniform persistent communication and randomized persistent communication protocols. We finally complement the analytical results with some numerical simulations.

[Read the original at arXiv →](https://arxiv.org/abs/2611.32928v1)
