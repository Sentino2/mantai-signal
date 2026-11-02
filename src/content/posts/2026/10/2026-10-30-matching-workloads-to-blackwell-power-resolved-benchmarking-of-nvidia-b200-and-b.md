---
title: "Matching Workloads to Blackwell: Power-Resolved Benchmarking of NVIDIA B200 and B300 across HPC and AI Workloads"
date: 2026-10-30T15:51:19+00:00
source: "arXiv"
source_url: "https://arxiv.org/abs/2610.41919v1"
ext_id: "arxiv:2610.41919v1"
tags: ["hardware", "models"]
summary: "We evaluate NVIDIA B200 and B300 (Blackwell Ultra) GPUs on two independent eight-GPU clusters, spanning computer-vision inference and training, LLM inference with Llama-3-8B and 70B~\cite{llama3}, and six production HPC codes. The B300 is not a uniform successor to the B200: it trails by up to 5.6$\times$ on convolutional inference, 8$\times$ on 3D vision transformer training, 24--27\% on 70B LLM "
---

We evaluate NVIDIA B200 and B300 (Blackwell Ultra) GPUs on two independent eight-GPU clusters, spanning computer-vision inference and training, LLM inference with Llama-3-8B and 70B~\cite{llama3}, and six production HPC codes. The B300 is not a uniform successor to the B200: it trails by up to 5.6$\times$ on convolutional inference, 8$\times$ on 3D vision transformer training, 24--27\% on 70B LLM throughput, and 16$\times$ on double-precision Quantum ESPRESSO. We resolve the convolutional deficit using per-GPU board power rather than throughput alone: on the affected workloads the B300 draws only 36--53\% of its 1100\,W envelope, whereas on ViT-Large, which it wins, both parts saturate at 95--97\% of TDP. Because our harness keeps inputs resident in device memory, a host-side data pipeline is excluded by construction, localizing the cause to per-kernel cost. Two B300 nodes of identical silicon differ by 2.1$\times$ in time-to-first-token solely from a development vLLM build. We give per-workload procurement guidance.

[Read the original at arXiv →](https://arxiv.org/abs/2610.41919v1)
