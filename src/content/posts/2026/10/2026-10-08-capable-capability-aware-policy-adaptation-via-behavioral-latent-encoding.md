---
title: "CAPABLE: Capability-Aware Policy Adaptation via Behavioral Latent Encoding"
date: 2026-10-08T13:46:52+00:00
source: "arXiv"
source_url: "https://arxiv.org/abs/2610.11971v1"
ext_id: "arxiv:2610.11971v1"
tags: ["hardware", "models"]
summary: "Vision-language-action (VLA) policies assume the embodiment on which they were trained and can fail when a joint fault changes how commanded actions are physically executed. Existing fault-recovery methods often require task-specific retraining, fault labels, explicit diagnosis, or privileged embodiment information. We introduce CAPABLE, a unified capability-aware adaptation framework for frozen V"
---

Vision-language-action (VLA) policies assume the embodiment on which they were trained and can fail when a joint fault changes how commanded actions are physically executed. Existing fault-recovery methods often require task-specific retraining, fault labels, explicit diagnosis, or privileged embodiment information. We introduce CAPABLE, a unified capability-aware adaptation framework for frozen VLAs that integrates self-supervised capability inference with residual reinforcement learning. CAPABLE infers capability, how much of the commanded motion each joint actually realizes and how that motion contributes to end-effector behavior, online from command-response history and kinematics using a temporal encoder shared across joints, Jacobian grounding, cross-joint attention, and self-supervised physical prediction. The resulting representation conditions a residual policy that adds bounded corrections to the VLA arm action without fault labels or faulty-joint identifiers. Across 28 LIBERO tasks, CAPABLE raises success on an actuator excluded from fault training from 24.8% to 59.3%, outperforming a parameter-matched global-history baseline by 17.4 points while preserving healthy performance. Leave-one-actuator-out experiments across six joints show that this transfer is not specific to one actuator, and additional evaluations characterize transfer to unseen fault families and demonstrate recovery on a physical Franka Panda. https://capable-vla.github.io/

[Read the original at arXiv →](https://arxiv.org/abs/2610.11971v1)
