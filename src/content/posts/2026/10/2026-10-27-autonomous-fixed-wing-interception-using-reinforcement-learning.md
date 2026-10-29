---
title: "Autonomous fixed-wing interception using reinforcement learning"
date: 2026-10-27T16:04:06+00:00
source: "arXiv"
source_url: "https://arxiv.org/abs/2610.37470v1"
ext_id: "arxiv:2610.37470v1"
tags: ["hardware", "models"]
summary: "Medium altitude, long endurance unmanned aerial systems such as Shahed-type strike drones are an unanswered threat in modern conflicts. Conventional air defense systems are too expensive to provide a feasible large-scale solution. Quadcopter interceptors are a cheap, battle-proven alternative, but their extremely limited flight time restricts them to low altitude targets at short range, whereas fi"
---

Medium altitude, long endurance unmanned aerial systems such as Shahed-type strike drones are an unanswered threat in modern conflicts. Conventional air defense systems are too expensive to provide a feasible large-scale solution. Quadcopter interceptors are a cheap, battle-proven alternative, but their extremely limited flight time restricts them to low altitude targets at short range, whereas fixed-wing platforms have the endurance to reach higher altitude targets from longer distances. However, such interceptors are still operated manually. Recent developments in learning-based controllers show potential for automation. In this work, a fixed-wing interceptor is presented that is controlled by a neural network that maps filtered monocular vision observations directly to actuator commands. The policy was trained in a custom Python environment using reinforcement learning and proximal policy optimization. The policy was then deployed on a fixed-wing platform and tested in real interception scenarios. As a baseline, two classical guidance controllers were also developed and tested in simulation. The policy is able to intercept targets both in simulation and in real flight. In simulation, the policy outperforms the classical controllers under most conditions. The interceptor was ultimately successfully validated in real flight by intercepting maneuvering fixed-wing targets. This novel system shows the potential of artificial intelligence for autonomous control of fixed-wing interceptor drones.

[Read the original at arXiv →](https://arxiv.org/abs/2610.37470v1)
