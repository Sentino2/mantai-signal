---
title: "A Secure dToF LiDAR SoC with Dual-Domain Fingerprinting and Event-Driven AFE Circuit Achieving Sensor-Level Attack Resilience"
date: 2026-10-02T16:40:26+00:00
source: "arXiv"
source_url: "https://arxiv.org/abs/2610.03562v1"
ext_id: "arxiv:2610.03562v1"
tags: ["models"]
summary: "Recent studies have shown that most commercial direct time-of-flight (dToF) LiDARs can be spoofed by injecting high-frequency laser pulses into the receiver, which can erase pedestrians from the point cloud. This paper presents the first dToF LiDAR system-on-chip (SoC) with integrated sensor-level hardware security against spoofing attacks. We propose Dual-Domain Fingerprinting (DDF), which emits "
---

Recent studies have shown that most commercial direct time-of-flight (dToF) LiDARs can be spoofed by injecting high-frequency laser pulses into the receiver, which can erase pedestrians from the point cloud. This paper presents the first dToF LiDAR system-on-chip (SoC) with integrated sensor-level hardware security against spoofing attacks. We propose Dual-Domain Fingerprinting (DDF), which emits laser pulse pairs whose time interval and amplitude ratio are both randomized and authenticates received echoes in this two-dimensional space, so that spoofed signals are rejected before they corrupt the ranging result. An Event-Driven AFE (ED-AFE) activates the ADC only around pulse peaks: it digitizes three samples around each peak with a triggered ADC at 1-GHz sampling and applies parabolic interpolation, achieving 1-cm distance resolution with a 99% reduction in ADC power. A time-modulated laser driver controls the laser amplitude from 10% to 100% by modulating the charge time of a laser capacitor, providing the microsecond-order amplitude modulation required by DDF. A LiDAR system with a 16-channel 65-nm CMOS prototype SoC demonstrates up to 120-m ranging and an AFE power of 3.1 mW per channel, 60% lower than prior art. In a proof-of-concept experiment in which the dual-domain authentication is applied to measured sensor data, 73% of the point cloud is protected under spoofing attack, compared with 0% without DDF.

[Read the original at arXiv →](https://arxiv.org/abs/2610.03562v1)
