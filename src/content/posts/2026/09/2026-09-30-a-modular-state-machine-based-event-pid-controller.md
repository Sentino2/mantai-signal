---
title: "A Modular State-Machine Based Event PID Controller"
date: 2026-09-30T16:55:10+00:00
source: "arXiv"
source_url: "https://arxiv.org/abs/2609.40152v1"
ext_id: "arxiv:2609.40152v1"
tags: ["hardware"]
summary: "In this paper, we present a modular proportional-integral-derivative (PID) controller whose computation and mode logic are executed by a higher-level state machine. Inspired by real-time safety-critical applications where computational load, actuator chattering, sensing error and noise are design challenges, the proposed algorithm wraps a standard PID inside a finite state machine with three state"
---

In this paper, we present a modular proportional-integral-derivative (PID) controller whose computation and mode logic are executed by a higher-level state machine. Inspired by real-time safety-critical applications where computational load, actuator chattering, sensing error and noise are design challenges, the proposed algorithm wraps a standard PID inside a finite state machine with three states (pidInit, ErrorOutRange, ErrorInRange). The goal is to regulate a desired reference within a safe region of operation while reducing actuator chattering and creating a sizable hold band over the range of operation. This design is modular and can be easily integrated into a higher-level state machine with multiple low-level loops and states. The algorithm also has low computational complexity and is suitable for embedded hardware deployment. We demonstrate the effectiveness of the algorithm in simulation on the two test benches of a published event-based PID benchmark. The algorithm computes the control updates significantly less often than the time-triggered PID and less often than both dominant event-driven controllers, while keeping a fairly equivalent control performance profile. Furthermore, we also present some experimental results of the designed algorithm for a real-time flow control.

[Read the original at arXiv →](https://arxiv.org/abs/2609.40152v1)
