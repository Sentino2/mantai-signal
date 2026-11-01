---
title: "Fundamental Limits of Sampling-Based Reachability: Geometry and Flow Distortion"
date: 2026-10-29T17:08:36+00:00
source: "arXiv"
source_url: "https://arxiv.org/abs/2610.40473v1"
ext_id: "arxiv:2610.40473v1"
tags: ["hardware", "models"]
summary: "Sampling-based reachability estimates reachable sets from finitely many simulated trajectory endpoints. Existing guarantees often control missed probability mass or approximation error relative to the convex hull of the reachable set, leaving the geometric error relative to the reachable set incompletely characterized. We study this error as a problem of support estimation under flow distortion. O"
---

Sampling-based reachability estimates reachable sets from finitely many simulated trajectory endpoints. Existing guarantees often control missed probability mass or approximation error relative to the convex hull of the reachable set, leaving the geometric error relative to the reachable set incompletely characterized. We study this error as a problem of support estimation under flow distortion. Our assumptions combine a uniform lower bound on the local volume density of the initial set, a lower bound on the sampling density, and a one-sided Lipschitz constant $μ$ for the vector field. These conditions admit initial sets with corners and dynamics that may expand or contract. In the fine-accuracy regime, $\tilde{\mathcal O}\bigl(2^ne^{nμT}(R/r)^n/(ρκ)\bigr)$ independent endpoint samples suffice for Hausdorff accuracy $r$ using the endpoint cloud. Here, $n$ is the state dimension, $T$ is the horizon, $R$ is the volume-equivalent radius, and $ρ$ and $κ$ quantify sampling density and local volume density. For $n\ge2$ and sufficiently small $κ$, a minimax lower bound over all estimators based only on independent endpoints matches these dependencies up to a dimension-dependent factor $2\cdot4^n$ and logarithmic factors, within the stated parameter range and when the state domain accommodates the construction. The exponential burden in dimension, and in the horizon for expanding systems, is therefore intrinsic to this observation model. Planar experiments illustrate the predicted effects of corners and contraction; robot-arm experiments show how empirical accuracy deteriorates with dimension.

[Read the original at arXiv →](https://arxiv.org/abs/2610.40473v1)
