---
title: "SkipLane: Write-Once, Conflict-Free Accumulation for Zero-Skipping CNN Engines on FPGAs"
date: 2026-11-10T18:50:51+00:00
source: "arXiv"
source_url: "https://arxiv.org/abs/2611.14495v1"
ext_id: "arxiv:2611.14495v1"
tags: ["models"]
summary: "Skipping zero activations saves multiplications in CNN accelerators, but it complicates accumulation: the products in a compressed input window belong to different output columns and must be merged. In our earlier engine, this merging was done by read-modify-write (RMW) of a row buffer, which made sparse inputs slower than dense ones even at 87% sparsity. Existing designs either merge kernel rows "
---

Skipping zero activations saves multiplications in CNN accelerators, but it complicates accumulation: the products in a compressed input window belong to different output columns and must be merged. In our earlier engine, this merging was done by read-modify-write (RMW) of a row buffer, which made sparse inputs slower than dense ones even at 87% sparsity. Existing designs either merge kernel rows through RMW or reduce bank conflicts with extra hardware, without eliminating them. SkipLane makes the entire accumulation path write-once. Each kernel row is processed in its own lane, which holds partial sums in three registers and retires up to three finished columns per cycle into memory banks that cannot conflict. Lanes and input channels are summed only at readout, so no partial sum is ever read back. Multipliers left idle by zero weights compute a second filter in the same pass. In RTL simulation, the engine stays within 0.5% of its frontend bound up to 70% sparsity and is 1.10-1.26$\times$ faster than an SCNN-style scatter accumulator with 18 banks and ideal RMW at 50-80% sparsity. Six engines meet 140 MHz on a PYNQ-Z2 using 21.1k LUTs and run LeNet-5 bit-exact on the board. For conv1, the engine needs 1.94$\times$ fewer cycles than a dense engine (1.26$\times$ faster end to end); for conv2, whose rows are only 13 pixels wide, it reaches 0.87$\times$ the dense speed.

[Read the original at arXiv →](https://arxiv.org/abs/2611.14495v1)
