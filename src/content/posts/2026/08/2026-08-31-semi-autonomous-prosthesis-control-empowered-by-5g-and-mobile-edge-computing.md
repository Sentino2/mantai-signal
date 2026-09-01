---
title: "Semi-Autonomous Prosthesis Control Empowered by 5G and Mobile Edge Computing"
date: 2026-08-31T16:03:46+00:00
source: "arXiv"
source_url: "https://arxiv.org/abs/2608.31021v1"
tags: ["hardware", "models"]
summary: "Prosthetic hands equipped with cameras can use computer vision to plan grasps automatically, reducing cognitive effort. However, running modern vision models on wearable devices is impractical due to power and processing constraints. We present the first prototype of a 5G-connected mobile edge computing (MEC)-enabled semi-autonomous prosthetic hand, which streams RGB-D images to an edge server for"
---

Prosthetic hands equipped with cameras can use computer vision to plan grasps automatically, reducing cognitive effort. However, running modern vision models on wearable devices is impractical due to power and processing constraints. We present the first prototype of a 5G-connected mobile edge computing (MEC)-enabled semi-autonomous prosthetic hand, which streams RGB-D images to an edge server for real-time grasp planning. Thirteen able-bodied participants performed pick-and-place tasks under six conditions: manual EMG control, on-device inference, wired Ethernet connectivity, and three 5G connectivity configurations (private 20 MHz network, private 100 MHz network, and a commercial 5G link) to the server. All network-based conditions performed similarly, achieving task times around 8.6 s (34% faster than manual control), failure rates of 20-38%, and 62% lower overall workload. On-device processing performed the worst with 10.3 s task time and a 76% failure rate due to slow embedded inference (3 fps vs. 6-20 fps over the network). Network latencies remained below 180 ms for private 5G and 270 ms for commercial 5G. All 5G configurations, including bandwidth-constrained and commercially variable networks, matched wired Ethernet performance while significantly outperforming both manual control and local processing, establishing 5G edge-offloading as a practical path to deploying compute-intensive prosthesis control.

[Read the original at arXiv →](https://arxiv.org/abs/2608.31021v1)
