---
title: "Analog Computing revisited: A fully analog and minimalistic Damage Detector for Ultrasonic Testing enabling Material-Integrated Structural Health Monitoring"
date: 2026-09-28T15:56:01+00:00
source: "arXiv"
source_url: "https://arxiv.org/abs/2609.35478v1"
ext_id: "arxiv:2609.35478v1"
tags: ["hardware", "models"]
summary: "Ultrasonic Testing (UT) is commonly used to detect damage in structures, e.g., metal plates. A sensor acquires Ultrasonic waves, e.g., by using PZT transducers. The time-resolved sensor signal must be processed with analog electronics, e.g., amplified and filtered. Commonly a digitalization follows using an Analog-to-Digital converter, finally processing the digital sensor signal, applying digital"
---

Ultrasonic Testing (UT) is commonly used to detect damage in structures, e.g., metal plates. A sensor acquires Ultrasonic waves, e.g., by using PZT transducers. The time-resolved sensor signal must be processed with analog electronics, e.g., amplified and filtered. Commonly a digitalization follows using an Analog-to-Digital converter, finally processing the digital sensor signal, applying digital signal processing, feature extraction, and Machine Learning by using powerful microprocessor systems. The disadvantages of digital processing systems are their high number of transistors (microchip area), energy consumption, state-dependent processing and therefore sensitivity to energy supply interruption. Beyond silicon electronics, printed organic electronics gains interest. But printed electronics is still limited to low transistor and electronic component counts (typically 100). We will investigate and demonstrate a fully analog signal processing and feature extraction system consisting of an analog Hilbert transform deriving the signal envelope, simple analog arithmetic calculations for feature extraction, and finally damage classification and regression using an analog Artificial Neural Network. We expect a full damage detection system with less than 100 transistors. We will test our damage detection system with PZT transducer signals from Steel plates with circular defects. The focus of this work is the analog computation of the signal envelope (using all-pass filter networks for approximation of the Hilbert transform) and the analog feature extraction as well as the prediction of damage, forming an analog computer which can perform in-sensor computation, computing without a digital computer.

[Read the original at arXiv →](https://arxiv.org/abs/2609.35478v1)
