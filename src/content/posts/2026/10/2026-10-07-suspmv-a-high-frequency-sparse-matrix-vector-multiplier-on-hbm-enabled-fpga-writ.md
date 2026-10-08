---
title: "SUSpMV: A High Frequency Sparse Matrix Vector Multiplier on HBM Enabled FPGA written in SUS"
date: 2026-10-07T16:51:55+00:00
source: "arXiv"
source_url: "https://arxiv.org/abs/2610.10403v1"
ext_id: "arxiv:2610.10403v1"
tags: ["hardware", "models", "security"]
summary: "SUSpMV is a Sparse Matrix Vector multiplication (SpMV) accelerator written in the upcoming HDL SUS. By leveraging SUS's unique latency counting and inference mechanism, SUSpMV could be designed with very deep pipelines yet small design complexity overhead. This enables an efficient implementation which employs all 32 HBM channels on the Alveo U280 FPGA at 400MHz for streaming matrix data into 32 C"
---

SUSpMV is a Sparse Matrix Vector multiplication (SpMV) accelerator written in the upcoming HDL SUS. By leveraging SUS's unique latency counting and inference mechanism, SUSpMV could be designed with very deep pipelines yet small design complexity overhead. This enables an efficient implementation which employs all 32 HBM channels on the Alveo U280 FPGA at 400MHz for streaming matrix data into 32 Compute Units (CUs). Input and output vectors are stored in DDR memory, which allows zero-overhead chaining of multiplications and increases overall system memory bandwidth by not sharing HBM bandwidth with the CUs.   A CU processes the SpMV in tiles of width 1024 and a dynamically chosen height, up to 32768. Each CU is capable of accumulating the multiplications with up to 6 separate matrix entries per cycle, resulting in the combined theoretical peak computational throughput of 153.6 GFLOPs. The matrix storage format is designed to exploit density variation within a given matrix by dynamically switching between one representation optimized for denser regions, and a second optimized for sparser regions, allowing jumps of up to 255 rows between each entry.   Evaluation demonstrates a 79% geometric mean improvement over prior work on the same platform. We achieve a peak throughput of 144.9 GFLOPs, or 94% of our theoretical computational throughput, compared to 98 GFLOPs reached by prior work.

[Read the original at arXiv →](https://arxiv.org/abs/2610.10403v1)
