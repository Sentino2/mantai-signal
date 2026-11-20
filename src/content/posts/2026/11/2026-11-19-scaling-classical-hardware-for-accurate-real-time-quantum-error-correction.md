---
title: "Scaling classical hardware for accurate real-time quantum error correction"
date: 2026-11-19T17:16:21+00:00
source: "arXiv"
source_url: "https://arxiv.org/abs/2611.26447v1"
ext_id: "arxiv:2611.26447v1"
tags: ["hardware", "models"]
summary: "Fault-tolerant quantum computation requires a classical decoder fast enough to process syndrome measurements at the rate at which they are generated, and to return its decisions with low latency. This is most demanding for superconducting processors, whose fast syndrome cycles force a trade-off between decoding speed and accuracy. Decoders fast enough to keep up sacrifice accuracy, which must be c"
---

Fault-tolerant quantum computation requires a classical decoder fast enough to process syndrome measurements at the rate at which they are generated, and to return its decisions with low latency. This is most demanding for superconducting processors, whose fast syndrome cycles force a trade-off between decoding speed and accuracy. Decoders fast enough to keep up sacrifice accuracy, which must be compensated for with larger codes and thus additional physical qubits. Here we introduce Rapids, a streaming neural decoder that is both fast and accurate. We achieve this by co-designing the decoder with a field-programmable gate array (FPGA): the network is built from operations that map cheaply onto the device and trained in its integer arithmetic. For the distance-19 surface code, Rapids decodes each round of syndromes in under a microsecond on a single FPGA, fast enough for superconducting processors, and returns its decisions with the low latency that fault-tolerant algorithms require. Its logical error rate is 240 times lower than that of existing real-time hardware decoders. The same design extends to the color code and the [[144,12,12]] bivariate-bicycle code, on which our decoder is 16 times more accurate than the real-time Relay decoder. We further show that the decoder scales: spread over several FPGAs or hardened into custom silicon, it becomes faster, more accurate, or able to decode larger codes. Classical hardware thus becomes a further resource, alongside qubits, that can be scaled to improve fault-tolerant quantum computers.

[Read the original at arXiv →](https://arxiv.org/abs/2611.26447v1)
