---
title: "Tropical Geometry-based ReLU Lyapunov Function and Controller Synthesis"
date: 2026-11-23T18:50:07+00:00
source: "arXiv"
source_url: "https://arxiv.org/abs/2611.31203v1"
ext_id: "arxiv:2611.31203v1"
tags: ["hardware", "models"]
summary: "We investigate the joint synthesis of neural network Lyapunov functions and stabilizing controllers for systems modeled as neural ordinary differential equations (neural ODEs) with ReLU activations. Our approach leverages tools from tropical geometry, an emerging analytical framework for characterizing properties of ReLU neural networks. To the best of our knowledge, this work is the first to intr"
---

We investigate the joint synthesis of neural network Lyapunov functions and stabilizing controllers for systems modeled as neural ordinary differential equations (neural ODEs) with ReLU activations. Our approach leverages tools from tropical geometry, an emerging analytical framework for characterizing properties of ReLU neural networks. To the best of our knowledge, this work is the first to introduce tropical geometry-based methods into control theory. We represent candidate Lyapunov functions as tropical quotients of tropical signomials, which allows us to enforce the equilibrium condition at the origin and formulate constraints ensuring positive definiteness over a prescribed region of interest. We construct a total Lie surface representing the Lie derivative of the candidate Lyapunov function along the neural ODE dynamics and formulate an optimization problem to find Lyapunov parameters that ensure its negativity throughout the region of interest. This enables the systematic search for Lyapunov functions satisfying the desired stability conditions. Finally, we extend this framework to jointly synthesize a ReLU neural network stabilizing controller and a neural Lyapunov function, providing a unified approach to stability analysis and controller synthesis. We validate our proposed method on several nonlinear systems approximated as neural ODEs, demonstrating applications to Lyapunov function synthesis as well as joint Lyapunov function and controller synthesis.

[Read the original at arXiv →](https://arxiv.org/abs/2611.31203v1)
