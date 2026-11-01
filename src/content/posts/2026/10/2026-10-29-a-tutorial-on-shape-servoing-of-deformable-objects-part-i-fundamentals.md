---
title: "A Tutorial on Shape Servoing of Deformable Objects-Part I: Fundamentals"
date: 2026-10-29T17:40:56+00:00
source: "arXiv"
source_url: "https://arxiv.org/abs/2610.40559v1"
ext_id: "arxiv:2610.40559v1"
tags: ["hardware", "models", "security"]
summary: "In robotics, shape control (or shape servoing) refers to the automatic manipulation of a deformable object to achieve a desired shape. It involves a feedback loop that exploits the relation between robot motion and changes in the measured shape. This relation, known as the interaction Jacobian or, in this context, the deformation Jacobian, depends on the object's mechanical properties, geometry, a"
---

In robotics, shape control (or shape servoing) refers to the automatic manipulation of a deformable object to achieve a desired shape. It involves a feedback loop that exploits the relation between robot motion and changes in the measured shape. This relation, known as the interaction Jacobian or, in this context, the deformation Jacobian, depends on the object's mechanical properties, geometry, and boundary conditions (e.g., where the object is grasped). Because these factors are often difficult to model accurately, the deformation Jacobian can be estimated locally from observed shape changes produced by commanded robot motions, without requiring a fine-tuned mechanical model. This article is the first of a two-part tutorial on data-driven Jacobian-based shape control of deformable objects. It introduces the central elements of the approach: the formulation of the shape-control problem, shape representation, estimation and online update of the deformation Jacobian, and a standard control law from the literature. It then assembles these elements into a complete shape-servoing loop, derives a local stability condition for this loop, and illustrates why some target shapes cannot be reached. Part II covers more advanced topics. Throughout both parts, a simulated planar example in which two robot arms manipulate an elastic rod observed by a camera illustrates the concepts.

[Read the original at arXiv →](https://arxiv.org/abs/2610.40559v1)
