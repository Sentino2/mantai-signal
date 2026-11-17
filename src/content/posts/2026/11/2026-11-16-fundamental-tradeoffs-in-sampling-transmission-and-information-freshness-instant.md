---
title: "Fundamental Tradeoffs in Sampling, Transmission and Information Freshness: Instantaneous Feedback"
date: 2026-11-16T18:31:04+00:00
source: "arXiv"
source_url: "https://arxiv.org/abs/2611.21547v1"
ext_id: "arxiv:2611.21547v1"
tags: ["hardware"]
summary: "We study a time-slotted generate-at-will status-update system over an erasure channel with transmission success probability $q$, subject to average sampling- and transmission-rate constraints $f_s$ and $f_r$, respectively. The sampler-transmitter pair jointly decides whether to idle, retransmit a stale packet, or replace it with a fresh sample. We derive a universal lower bound on the optimal aver"
---

We study a time-slotted generate-at-will status-update system over an erasure channel with transmission success probability $q$, subject to average sampling- and transmission-rate constraints $f_s$ and $f_r$, respectively. The sampler-transmitter pair jointly decides whether to idle, retransmit a stale packet, or replace it with a fresh sample. We derive a universal lower bound on the optimal average age of information, analyze a class of stationary randomized policies, and obtain an optimal policy within this class that provides a $4$-approximation guarantee. The joint problem reduces to the sampling-constrained problem when $f_s\leq qf_r$ and the transmission-constrained problem when $f_s\geq f_r$. For $qf_r<f_s<f_r$, we formulate a constrained Markov decision process (CMDP) and introduce the class $\barΠ$ of $(W,R)$ policies, where $W$ specifies a waiting threshold for transmission and $R$ specifies a packet-replacement threshold. We prove that, for every choice of Lagrange multipliers, the corresponding Lagrangian-relaxed Markov decision process admits an optimal policy in $\barΠ$. We then formulate a linear program (LP) over distributions of $(W,R)$ policies and prove that choosing a policy according to an optimal LP solution yields an optimal CMDP policy. Moreover, there exists an optimal LP solution assigning positive probability to at most three $(W,R)$ policies. Since $\barΠ$ is countably infinite, for every $ε>0$ we construct a finite subset $\barΠ_ε\subset\barΠ$ and show that the LP restricted to this set yields an $ε$-optimal policy. Finally, we derive a stronger pair of lower bounds by considering systems with only the sampling-rate or transmission-rate constraint. Using these bounds, we construct a policy randomizing among four $(W,R)$ policies with a $2$-approximation guarantee for $qf_r<f_s<f_r$.

[Read the original at arXiv →](https://arxiv.org/abs/2611.21547v1)
