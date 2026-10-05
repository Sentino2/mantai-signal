---
title: "DR-IPC: Disturbance-Resilient Integrated Planning and Control for LiDAR-Based Quadrotor Navigation"
date: 2026-10-02T16:16:43+00:00
source: "arXiv"
source_url: "https://arxiv.org/abs/2610.03530v1"
ext_id: "arxiv:2610.03530v1"
tags: ["hardware", "models"]
summary: "LiDAR-based quadrotor navigation in cluttered environments remains challenging under external disturbances, particularly when obstacle-aware motion generation and disturbance-rejection control are handled in separate layers. This article presents disturbance-resilient integrated planning and control (DR-IPC), which combines lightweight path guidance with nonlinear model predictive control (NMPC) t"
---

LiDAR-based quadrotor navigation in cluttered environments remains challenging under external disturbances, particularly when obstacle-aware motion generation and disturbance-rejection control are handled in separate layers. This article presents disturbance-resilient integrated planning and control (DR-IPC), which combines lightweight path guidance with nonlinear model predictive control (NMPC) to directly generate angular velocity and thrust. An interconnected extended Kalman filter and nonlinear disturbance observer jointly provide filtered state estimates and reconstructed disturbances for NMPC prediction. The resulting formulation unifies nonlinear quadrotor dynamics, actuator constraints, local motion generation, and penalised safe-flight-corridor residuals without requiring a separate trajectory-optimization stage. Gazebo and MARSIM simulations, together with indoor and outdoor experiments, validate DR-IPC under wind, suspended payloads, narrow passages, ball impacts and reactive avoidance of a dynamic obstacle. In multi-goal navigation with disturbances, DR-IPC increases the number of completed missions from 1/10 to 9/10 in Gazebo and reduces the altitude RMSE from 0.34 to 0.01 m in experiments. The complete system operates onboard at 100 Hz. Supplementary videos are available on the project page https://drpp316.github.io/DR-IPC-Page/, and the source code will be released.

[Read the original at arXiv →](https://arxiv.org/abs/2610.03530v1)
