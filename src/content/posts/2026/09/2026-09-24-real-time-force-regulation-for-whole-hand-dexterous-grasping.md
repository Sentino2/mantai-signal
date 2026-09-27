---
title: "Real-Time Force Regulation for Whole-Hand Dexterous Grasping"
date: 2026-09-24T16:31:51+00:00
source: "arXiv"
source_url: "https://arxiv.org/abs/2609.30082v1"
ext_id: "arxiv:2609.30082v1"
tags: ["hardware", "models"]
summary: "Robust dexterous grasping requires maintaining physical stability despite contacts interactively evolving across the entire hand. A precomputed force distribution can easily fail under object motion, modeling errors, or external disturbances. In this paper, we present a framework for real-time force regulation over dynamically changing whole-hand contacts. Our method geometrically estimates contac"
---

Robust dexterous grasping requires maintaining physical stability despite contacts interactively evolving across the entire hand. A precomputed force distribution can easily fail under object motion, modeling errors, or external disturbances. In this paper, we present a framework for real-time force regulation over dynamically changing whole-hand contacts. Our method geometrically estimates contacts across all hand links using a tracked object model and proprioception, without requiring tactile sensing at those contacts. It repeatedly recomputes the desired contact-force distribution subject to friction constraints, actuator limits, and an actuation-consistency constraint motivated by classical whole-limb force analysis. We integrate this force-regulation controller with reactive reaching, enabling the hand to acquire a grasp, maintain it under disturbances, and regrasp after losing the object. Simulation experiments without gravity demonstrate improved grasp retention over fixed-allocation and fingertip-only execution under controlled perturbations, while real-world experiments on a 27-DoF arm-hand system demonstrate grasp maintenance and recovery under human-applied disturbances as contacts evolve across the whole hand. Project page: https://sangminkim-99.github.io/reactive-grasp-whole-hand/

[Read the original at arXiv →](https://arxiv.org/abs/2609.30082v1)
