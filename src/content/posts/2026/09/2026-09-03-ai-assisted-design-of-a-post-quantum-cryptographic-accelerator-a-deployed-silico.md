---
title: "AI-Assisted Design of a Post-Quantum Cryptographic Accelerator: A Deployed-Silicon Case Study"
date: 2026-09-03T16:34:50+00:00
source: "arXiv"
source_url: "https://arxiv.org/abs/2609.04058v1"
ext_id: "arxiv:2609.04058v1"
tags: ["hardware", "models"]
summary: "Post-quantum migration is mandated on published timelines, and silicon that ships with a defect cannot be patched remotely. The standard acceptance gate cannot detect an entire class of ML-DSA defects. Signing resamples until a candidate meets its norm bounds, so the executed path varies with the message, whereas known-answer tests (KATs) sample fixed values and reach only the depths their seeds t"
---

Post-quantum migration is mandated on published timelines, and silicon that ships with a defect cannot be patched remotely. The standard acceptance gate cannot detect an entire class of ML-DSA defects. Signing resamples until a candidate meets its norm bounds, so the executed path varies with the message, whereas known-answer tests (KATs) sample fixed values and reach only the depths their seeds trigger. Our accelerator passed its full KAT regression while carrying a norm check that outran block-RAM latency, leaving each candidate's final coefficients unverified; the escape surfaced at reject-loop iteration 5. The blind spot lies in the instrument, not the engineer; care cannot remove it. We replace that gate. A byte-exact golden-reference oracle paired with randomized adversarial soak drives the rejection loop past any fixed vector, closing the gap: 301,343 data-dependent signings, zero escapes. Because the gate judges artifacts and never authors, trust becomes separable from authorship, making AI authorship an answerable question. We report 232 logged experiments in which an agentic large language model drove a unified ML-KEM-768 and ML-DSA-65 accelerator with on-chip key custody from RTL to PCIe bring-up on one Kintex-7 XC7K160T, shipped at 98.5% slice occupancy. Success was 71.6%, following a hardware-coupling gradient, 77-85% for documentation and research against 50-53% for synthesis and bring-up, which observability can explain: failure concentrates where corrective signals are physical-side only. That so unreliable an author produced an artifact byte-exact across all six FIPS operations -- its deployed baseline surviving the same 779,945-check zero-failure soak -- is the claim.

[Read the original at arXiv →](https://arxiv.org/abs/2609.04058v1)
