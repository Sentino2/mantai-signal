---
title: "Performance Characterization of SPEC CPU 2026 on AMD EPYC 9755 Processor"
date: 2026-09-01T16:56:19+00:00
source: "arXiv"
source_url: "https://arxiv.org/abs/2609.01527v1"
tags: ["models"]
summary: "SPEC CPU 2026 is the first major update to the industry-standard CPU benchmark suite since 2017. This paper presents the first microarchitecture based performance characterization of the new suite, conducted on AMD EPYC 'Zen 5', also the first SPEC CPU characterization study on this microarchitecture. Using a multi-lens methodology spanning pipeline efficiency, control flow behavior, cache hierarc"
---

SPEC CPU 2026 is the first major update to the industry-standard CPU benchmark suite since 2017. This paper presents the first microarchitecture based performance characterization of the new suite, conducted on AMD EPYC "Zen 5", also the first SPEC CPU characterization study on this microarchitecture. Using a multi-lens methodology spanning pipeline efficiency, control flow behavior, cache hierarchy pressure, and instruction mix, we analyze both SPECrate and SPECspeed suites. We introduce scale analysis, comparing single-copy to full-system behavior to expose system-level bottlenecks invisible to conventional characterization. Our analysis reveals substantial behavioral diversity across the suite, and the multi-lens analysis identifies three distinct behavioral clusters: frontend control-flow-dominated workloads that stress branch predictor throughput rather than accuracy, high-efficiency compute workloads that suffer SMT contention at scale, and memory bandwidth-bound workloads with poor L3 filtering even at single-copy. Scale-dependent effects, including SMT dispatch contention causing throughput reduction and L3 capacity interference, emerge only at full system utilization. This work establishes an empirical foundation for architectural research and workload-driven design decisions targeting next-generation datacenter processors.

[Read the original at arXiv →](https://arxiv.org/abs/2609.01527v1)
