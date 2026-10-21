---
title: "RPolyPlan: A Unified Global Floorplanning and Legalization Framework for Rectilinear Soft Modules"
date: 2026-10-20T14:29:26+00:00
source: "arXiv"
source_url: "https://arxiv.org/abs/2610.28276v1"
ext_id: "arxiv:2610.28276v1"
tags: ["models"]
summary: "Floorplanning with rectilinear soft modules improves area utilization and wirelength by allowing modules to adapt to rectilinear polygon (RPoly) shapes. Existing methods typically construct rectilinear polygons through incremental refinement after obtaining a rectangular global solution, which confines polygon exploration to the neighborhood induced by the initial floorplan. This paper presents RP"
---

Floorplanning with rectilinear soft modules improves area utilization and wirelength by allowing modules to adapt to rectilinear polygon (RPoly) shapes. Existing methods typically construct rectilinear polygons through incremental refinement after obtaining a rectangular global solution, which confines polygon exploration to the neighborhood induced by the initial floorplan. This paper presents RPolyPlan, a unified framework for outline-free and fixed-outline floorplanning that directly incorporates continuously deformable rectilinear polygons into global floorplanning. To enable direct polygon optimization, we introduce a structured continuous representation and a differentiable polygon shaping model that dynamically optimizes rectilinear module shapes based on overlaps, making continuous shape optimization feasible for gradient-based global floorplanning. An augmented Lagrangian formulation robustly handles the coupled inequality constraints, provides theoretical convergence guarantees, and reduces dependence on manual penalty-parameter tuning. During legalization, minimum-cost flow and rectangular decomposition determine the target areas of subrectangles, and horizontal and vertical constraint graphs encode their geometric relations. The resulting convex legalization formulation satisfies the area, shape, separation, connectivity, and outline constraints while minimizing either the chip area or the displacement from the global floorplanning solution. Experiments on the GSRC, MCNC, and ICCAD 2023 contest benchmarks demonstrate that RPolyPlan reduces HPWL over the evaluated state-of-the-art methods by 7% and 6% in fixed-outline and outline-free experiments, respectively.

[Read the original at arXiv →](https://arxiv.org/abs/2610.28276v1)
