---
title: "TileDRAM: Compiler-Controlled Tile-to-DRAM Layouts for 3D DRAM GPGPUs"
date: 2026-10-16T17:06:31+00:00
source: "arXiv"
source_url: "https://arxiv.org/abs/2610.23767v1"
ext_id: "arxiv:2610.23767v1"
tags: ["models"]
summary: "Modern GPU compilers expose rich layout abstractions for mapping tensors to threads and on-chip resources, but compute-unit-local (CU-local) 3D DRAM architectures lack a corresponding abstraction for specifying how operand-tile data are   arranged within the DRAM address space. Without such an abstraction, conventional placement under the existing DRAM address mapping can subject structured tile a"
---

Modern GPU compilers expose rich layout abstractions for mapping tensors to threads and on-chip resources, but compute-unit-local (CU-local) 3D DRAM architectures lack a corresponding abstraction for specifying how operand-tile data are   arranged within the DRAM address space. Without such an abstraction, conventional placement under the existing DRAM address mapping can subject structured tile accesses to severe row-buffer conflicts. We present TileDRAM, a compiler-runtime   toolchain that introduces tile-to-DRAM layouts as a compiler-visible abstraction for DRAM placement. TileDRAM extends the GPU Linear Layout abstraction from compute-side mapping targets to DRAM placement coordinates and selects layouts per   tile access signature, using recurring tile-local access behavior as the specialization unit. Since row-buffer locality depends on ordered request history, TileDRAM evaluates candidate layouts through their row-buffer behavior under fixed   DRAM address mappings. Accesses under the selected layouts are realized through ordinary address arithmetic, without new address-remapping hardware or ISA support. In full-trace replay on Accel-Sim/Ramulator2 across 108 mixture-of-experts   (MoE) feed-forward network (FFN) cases, TileDRAM reduces the request-weighted row-conflict rate from 75.7% to 15.2% and achieves a 1.77x geomean speedup. Retargeting six traces to six 3D DRAM organizations yields a 2.20x geomean speedup   under the same compiler abstraction. On an RTX 3090, address transformation adds 0.17% geomean overhead over identity.

[Read the original at arXiv →](https://arxiv.org/abs/2610.23767v1)
