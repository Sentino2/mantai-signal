---
title: "Catscan: Visualizing Pipelines of CPU Performance Simulation"
date: 2026-10-01T17:35:20+00:00
source: "arXiv"
source_url: "https://arxiv.org/abs/2610.02121v1"
ext_id: "arxiv:2610.02121v1"
tags: ["hardware", "models"]
summary: "Processor pipeline visualization tools are routine inside industry CPU teams, but few of them are described or released publicly. As a result, students, researchers, and other practitioners rarely see the tooling that processor architects use to debug performance before silicon. This paper describes two pieces of Ampere Computing's performance- analysis infrastructure that we have released to the "
---

Processor pipeline visualization tools are routine inside industry CPU teams, but few of them are described or released publicly. As a result, students, researchers, and other practitioners rarely see the tooling that processor architects use to debug performance before silicon. This paper describes two pieces of Ampere Computing's performance- analysis infrastructure that we have released to the community as open source: event streams, a simulator-output format, and Catscan, an interactive viewer built around that format. Event streams record microarchitectural activity as typed events connected by transaction relationships, so a user can move between a symptom and the instruction, uop, or memory transaction that explains it. Catscan uses that structure to support resource- and transaction-oriented views, persistent highlighting, domain-specific search, comparative trace synchronization, and other workflows used during product development. In this paper we report the design choices that survived production use, the limitations we encountered, and the lessons we think are useful for future microarchitectural visualization tools.

[Read the original at arXiv →](https://arxiv.org/abs/2610.02121v1)
