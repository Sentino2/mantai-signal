---
title: "Neuromorphic architectures as numerical solvers for computational neuroscience"
date: 2026-08-28T14:43:41+00:00
source: "arXiv"
source_url: "https://arxiv.org/abs/2608.28387v1"
tags: ["models"]
summary: "Neuromorphic computing is closely associated with spiking neuronal networks. However, an alternative class of so-called 'rate-based' models arising from computational neuroscience and machine learning forgoes spiking interactions and instead relies on continuous coupling between neurons. Existing neuromorphic implementations designed around spike-based interactions are not well-suited for emulatin"
---

Neuromorphic computing is closely associated with spiking neuronal networks. However, an alternative class of so-called "rate-based" models arising from computational neuroscience and machine learning forgoes spiking interactions and instead relies on continuous coupling between neurons. Existing neuromorphic implementations designed around spike-based interactions are not well-suited for emulating such models. Here view the distributed simulation of these models as message-passing algorithms on parallel hardware. Leveraging prior art in numerical algorithms and distributed simulation, we outline steps that enable the design of efficient digital neuromorphic accelerators for non-spiking neuronal models. In particular, we show that multi-bit packets, rather than spikes, are the most efficient communication strategy in packet-switched networks and that compared to basic numerical integration methods, higher-order differential equation solvers decrease both computation and communication costs while achieving lower numerical error, but that these benefits are ultimately limited by arithmetic precision. Using our proposed design principles, we convert an existing neuromorphic architecture into a distributed numerical solver - a spikeless neuromorphic system - for continuously-coupled neuronal models. We thereby demonstrate that our theoretical considerations indeed translate into practical advantages, namely reduced energy consumption and delay.

[Read the original at arXiv →](https://arxiv.org/abs/2608.28387v1)
