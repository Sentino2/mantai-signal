---
title: "DiSKO: Distribution Steering for Nonlinear Systems using the Koopman Operator"
date: 2026-11-12T18:55:31+00:00
source: "arXiv"
source_url: "https://arxiv.org/abs/2611.17301v1"
ext_id: "arxiv:2611.17301v1"
tags: ["hardware", "models", "security"]
summary: "This paper studies the problem of data-driven covariance steering for stochastic, nonlinear dynamical systems. We utilize Koopman operator theory to learn, directly from data, an approximate linear representation of the nonlinear dynamics in a lifted space of observable functions of the state. By exploiting this linear model, we design controllers for the mean and covariance of the underlying nonl"
---

This paper studies the problem of data-driven covariance steering for stochastic, nonlinear dynamical systems. We utilize Koopman operator theory to learn, directly from data, an approximate linear representation of the nonlinear dynamics in a lifted space of observable functions of the state. By exploiting this linear model, we design controllers for the mean and covariance of the underlying nonlinear system by utilizing linear distribution steering algorithms. To account for approximation errors in the learned dynamics and the ambiguity in the disturbance distribution induced in the lifted space, we formulate the problem as a distributionally robust covariance steering problem. Furthermore, we leverage a deep neural network (DNN) to simultaneously learn the Koopman observables and the linear model parameters, thus eliminating the need for manual observables basis selection while also reducing the dimensionality of the lifted representation. Additionally, we can promote desirable model properties, such as stability, during DNN training. We demonstrate the effectiveness of the proposed framework via numerical simulations.

[Read the original at arXiv →](https://arxiv.org/abs/2611.17301v1)
